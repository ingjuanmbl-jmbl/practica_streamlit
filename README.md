# 📊 Dashboard de Ventas con Streamlit

> Práctica de desarrollo de dashboards interactivos con Python,
> combinando análisis de datos y visualización en una app web desplegada en la nube.

🔗 **Demo en vivo:** https://practicaapp-fsz5qdnwwvy4y7oskfyhxj.streamlit.app/

---

## 💡 ¿De qué trata este proyecto?

Como parte de mi proceso de aprendizaje,
construí este dashboard interactivo de ventas que permite explorar
métricas clave de negocio de forma visual y dinámica, sin necesidad
de conocimientos técnicos para usarlo. Basado en un data Set de ventas sintetico

El reto principal fue conectar el análisis de datos en Python
con una interfaz web funcional, desplegada públicamente en la nube,
todo sin usar frameworks web tradicionales como Flask o Django.

---

## 🛠️ Stack tecnológico

| Tecnología | Rol en el proyecto |
|---|---|
| **Streamlit** | Framework para convertir el script Python en app web |
| **Pandas** | Manipulación y filtrado del dataset |
| **NumPy** | Generación del dataset sintético de ventas |
| **Plotly** | Gráficos interactivos (tendencia, barras) |
| **Jupyter Notebook** | Exploración inicial de los datos |
| **Cursor** | Entorno de desarrollo de la app |
| **GitHub** | Control de versiones y repositorio del proyecto |
| **Streamlit Community Cloud** | Despliegue gratuito de la app en producción |

---

## 📊 ¿Qué responde este dashboard?

- 📈 ¿Cuál es la tendencia de ventas en el tiempo?
- 📦 ¿Qué productos se venden más?
- 👤 ¿Quiénes son los vendedores con mayor facturación?

Todo filtrable en tiempo real por **región**, **vendedor** y **rango de fechas**.

---

## 🧠 Aprendizajes clave

- Cómo funciona el modelo de re-ejecución de Streamlit
- Uso de `@st.cache_data` para optimizar rendimiento
- Integración de Pandas + Plotly dentro de una app web
- Despliegue de una app Python en la nube desde GitHub

---

## ⚙️ Correr el proyecto localmente
```bash
git clone https://github.com/tu-usuario/dashboard-ventas.git
cd dashboard-ventas
pip install -r requirements.txt
streamlit run dashboard.py
```

---

## 👤 Autor

**Ing. Juan Manuel Betancur Lopez**
[LinkedIn](https://www.linkedin.com/in/ingjuanmbl/) · [GitHub](https://github.com/ingjuanmbl-jmbl)