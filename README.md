# Análisis de Anuncios de Vehículos

Este proyecto es una aplicación web interactiva desarrollada en Python que permite realizar un análisis exploratorio de datos (EDA) sobre un conjunto de datos de anuncios de venta de coches en EE. UU. La aplicación está construida con **Streamlit** y desplegada en la nube mediante **Render**.

### [Ver la aplicación en vivo en Render](https://anuncios-autos.onrender.com/) 

---

## 📋 Descripción del Proyecto
El objetivo principal es demostrar habilidades en el desarrollo de software, incluyendo la gestión de entornos virtuales, el uso de librerías de visualización de datos y el despliegue de aplicaciones web funcionales. 

La herramienta permite a los usuarios interactuar con los datos de forma dinámica, visualizando distribuciones y correlaciones clave en el mercado automotriz.

## 🚀 Funcionalidades
La aplicación incluye:
* **Encabezado informativo:** Título y descripción clara de la herramienta.
* **Histograma Interactivo:** Visualización de la distribución del millaje (`odometer`) de los vehículos.
* **Gráfico de Dispersión:** Análisis de la relación entre el precio (`price`) y el millaje del vehículo.
* **Interactividad con Checkboxes:** El usuario decide qué gráficos generar mediante casillas de verificación, optimizando el rendimiento de la aplicación.

## 🛠 Tecnologías y Librerías
* **Python 3.x**
* **Pandas:** Para la manipulación y carga de datos.
* **Streamlit:** Framework para la creación del cuadro de mando interactivo.
* **Plotly Express:** Librería para la generación de gráficos interactivos de alta calidad.
* **Git / GitHub:** Control de versiones.
* **Render:** Plataforma de despliegue (Hosting).

---

## 📂 Estructura del Repositorio
```text
.
├── app.py              # Código principal de la aplicación Streamlit
├── notebooks/
│   └── EDA.ipynb       # Pruebas iniciales y análisis exploratorio
├── vehicles_us.csv     # Conjunto de datos original
├── requirements.txt    # Dependencias necesarias para el despliegue
├── .gitignore          # Archivos excluidos del repositorio (ej. entornos virtuales)
└── README.md           # Documentación del proyecto
