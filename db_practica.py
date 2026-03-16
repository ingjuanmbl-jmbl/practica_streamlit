#Bloque 01: Importar lobrerias necesarias, configuracion de la pagina, cargue y filtrado del dataset
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

#---------CONFIGURACIÓN DE LA PÁGINA-----------
st.set_page_config(
    page_title="DashBoard de vetas",
    page_icon= "📊",
    layout="wide"   #Ocupa el ancho del navegador
)


#------CARGA DEL DATA SET
@st.cache_data    #Solo caraga el data set una vez
def cargar_datos():
    df = pd.read_csv("ventas_sint.csv")
    df['FECHA'] = pd.to_datetime(df['FECHA']) #Los csv no guardan tipo de fecha por lo que debemos convertir el dato
    return df

df = cargar_datos()

#BLOQUE 2: SIDEBAR
with st.sidebar:
    st.title("FILTROS")

    #Asignacion de valores para los filtros
    regiones = st.multiselect(
        "FILTRAR POR REGION",
        options=df['REGION'].unique(),
        default=df['REGION'].unique(),
    )
    vendedores = st.multiselect(
    "FILTRAR POR VENDEDOR",
    options=df['VENDEDOR'].unique(),
    default=df['VENDEDOR'].unique()
    )

    #Entradas de fecha
    
    fecha_min = df['FECHA'].min().date()
    fecha_max = df['FECHA'].max().date()

    rango_fechas = st.date_input(
        "FILTRAR POR RANGO DE FECHAS",
        value=(fecha_min, fecha_max), #Valor inicial -> Rango completo
        min_value=fecha_min,
        max_value=fecha_max
    )

#Aplicar filtros

df_filtrado = df[
    (df['REGION'].isin(regiones)) &
    (df['VENDEDOR'].isin(vendedores))&
    (df['FECHA'].dt.date >=rango_fechas[0]) &
    (df['FECHA'].dt.date <=rango_fechas[1])
]

#-------------------BLOQUE 3: METRICAS CLAVE

#Titulo principal
st.title("📊 Dash Board de Ventas")
st.markdown("---")

#Fila de metricas
col1,col2,col3 =st.columns(3) #Este metodo abre un panel para colocar n cantidad de metricas

with col1:
    st.metric(
        label = "VENTAS TOTALES",
        value=f"${df_filtrado['VENTA_TOTAL'].sum():,.0f}"
    )

with col2:

    mejor_vendedor = (
        df_filtrado.groupby("VENDEDOR")["VENTA_TOTAL"]
        .sum().idxmax()
    )
    st.metric(
        label = "MEJOR VENDEDOR",
        value=mejor_vendedor
    )

with col3:
    mejor_producto = (
        df_filtrado.groupby("PRODUCTO")["CANTIDAD_VENDIDA"]
        .sum().idxmax()
    )
    st.metric(
        label="PRODUCTO ESTRELLA",
        value=mejor_producto
    )

st.markdown("---")

#BLOQUE 4: Graficos
st.subheader("Tendencia Venta Total")

#Grafico 1: Tendencia de ventas 
ventas_por_fecha = (
    df_filtrado.groupby("FECHA")["VENTA_TOTAL"]
    .sum().reset_index()
)

fig_tendencia = px.line(
    ventas_por_fecha,
    x="FECHA",
    y= "VENTA_TOTAL",
    title = "Comportamiento diario del las ventas",
    labels={"venta Total": "Ventas (&)", "Fecha":"Fecha"}
)

st.plotly_chart(fig_tendencia, use_container_width=True)
st.markdown("---")

#Siguientes graficos en columnas
col_izq, col_der = st.columns(2)

with col_izq:
    st.subheader("Vendedores Top")

    vendedores_top = (
        df_filtrado.groupby("VENDEDOR")["VENTA_TOTAL"]
        .sum().reset_index()
        .sort_values("VENTA_TOTAL", ascending=True)
    )

    fig_vendedores_top = px.bar(
        vendedores_top,
        x="VENTA_TOTAL",
        y="VENDEDOR",
        orientation="h",
        title="Top vendedores por venta total",
        labels={"VENTA_TOTAL": "Ventas ($)", "VENDEDOR": "Vendedor"}
    )

    st.plotly_chart(fig_vendedores_top, use_container_width=True)

with col_der:
    st.subheader("Productos más vendidos")
    productos=(
        df_filtrado.groupby("PRODUCTO")["CANTIDAD_VENDIDA"]
        .sum().reset_index()
        .sort_values("CANTIDAD_VENDIDA", ascending=False)
    )

    fig_productos = px.bar(
        productos,
        x="PRODUCTO",
        y="CANTIDAD_VENDIDA",
        color="PRODUCTO",
        title="Comportamiento de unidades vendidas por producto",
        labels={"CANTIDAD VENDIDA": "TOTAL UNIDADES","PRODUCTO": "PRODUCTO"}
    )
    st.plotly_chart(fig_productos, use_container_width=True)

