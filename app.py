{\rtf1\ansi\ansicpg1252\cocoartf2867
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import pandas as pd\
import plotly.express as px\
import streamlit as st\
\
# Leer los datos\
car_data = pd.read_csv('vehicles_us.csv')\
\
# Encabezado principal\
st.header('Cuadro de Mando de Anuncios de Venta de Coches')\
\
# Subt\'edtulo o descripci\'f3n\
st.write('Analiza la relaci\'f3n entre el millaje, el precio y otras variables de los veh\'edculos en venta.')\
\
# Crear casillas de verificaci\'f3n (Checkboxes)\
build_histogram = st.checkbox('Construir un histograma del od\'f3metro')\
build_scatter = st.checkbox('Construir un gr\'e1fico de dispersi\'f3n (Precio vs Od\'f3metro)')\
\
if build_histogram: # si la casilla de histograma est\'e1 seleccionada\
    st.write('Visualizando la distribuci\'f3n del kilometraje (od\'f3metro)')\
    # crear un histograma\
    fig_hist = px.histogram(car_data, x="odometer")\
    # mostrar gr\'e1fico interactivo\
    st.plotly_chart(fig_hist, use_container_width=True)\
\
if build_scatter: # si la casilla de dispersi\'f3n est\'e1 seleccionada\
    st.write('Visualizando la relaci\'f3n entre precio y kilometraje')\
    # crear un gr\'e1fico de dispersi\'f3n\
    fig_scatter = px.scatter(car_data, x="odometer", y="price")\
    # mostrar gr\'e1fico interactivo\
    st.plotly_chart(fig_scatter, use_container_width=True)}