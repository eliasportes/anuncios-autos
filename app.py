import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado principal
st.header('Cuadro de Mando de Anuncios de Venta de Coches')

# Subtítulo o descripción
st.write('Analiza la relación entre el millaje, el precio y otras variables de los vehículos en venta.')

# Crear casillas de verificación (Checkboxes)
build_histogram = st.checkbox('Construir un histograma del odómetro')
build_scatter = st.checkbox('Construir un gráfico de dispersión (Precio vs Odómetro)')

if build_histogram: # si la casilla de histograma está seleccionada
    st.write('Visualizando la distribución del kilometraje (odómetro)')
    # crear un histograma
    fig_hist = px.histogram(car_data, x="odometer")
    # mostrar gráfico interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

if build_scatter: # si la casilla de dispersión está seleccionada
    st.write('Visualizando la relación entre precio y kilometraje')
    # crear un gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    # mostrar gráfico interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)