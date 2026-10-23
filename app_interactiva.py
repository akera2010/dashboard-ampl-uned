import streamlit as st
import pandas as pd
import plotly.express as px
import glob

# Configuración de la página web
st.set_page_config(page_title="Dashboard AMPL - Sandra Blanco", layout="wide")

# Título principal
st.title("📊 Dashboard Interactivo de Optimización")
st.markdown("**Autora:** Sandra Blanco | **Asignatura:** Métodos Analíticos (UNED 2026)")
st.markdown("---")

# Función mágica para buscar los CSV en cualquier carpeta
def cargar_datos(nombre_csv):
    archivos = glob.glob(f'**/{nombre_csv}', recursive=True)
    if archivos:
        return pd.read_csv(archivos[0])
    return None

# --- FILA 1: PRODUCCIÓN ---
st.header("1. Optimización de Producción (Maximizar)")
col1, col2 = st.columns(2)

with col1:
    df1 = cargar_datos('resultados1.csv')
    if df1 is not None:
        fig1 = px.bar(df1, x=df1.columns[0], y=df1.columns[1], 
                      title="Ej. 1: Max Beneficio Básico (300€)",
                      color=df1.columns[1], color_continuous_scale=['#d3d3d3', '#2ca02c'])
        st.plotly_chart(fig1, use_container_width=True)

    df5 = cargar_datos('resultados5.csv')
    if df5 is not None:
        fig5 = px.bar(df5, x=df5.columns[0], y=df5.columns[1], 
                      title="Ej. 5: Múltiples Recursos (1400€)",
                      color=df5.columns[1], color_continuous_scale=['#d3d3d3', '#2ca02c'])
        st.plotly_chart(fig5, use_container_width=True)

with col2:
    df2 = cargar_datos('resultados2.csv')
    if df2 is not None:
        fig2 = px.bar(df2, x=df2.columns[0], y=df2.columns[1], 
                      title="Ej. 2: Añadir Producto D (375€)",
                      color=df2.columns[1], color_continuous_scale=['#d3d3d3', '#2ca02c'])
        st.plotly_chart(fig2, use_container_width=True)

    df6 = cargar_datos('resultados6.csv')
    if df6 is not None:
        fig6 = px.bar(df6, x=df6.columns[0], y=df6.columns[1], 
                      title="Ej. 6: Embalaje Limitado (1350€)",
                      color=df6.columns[1], color_continuous_scale=['#d3d3d3', '#2ca02c'])
        st.plotly_chart(fig6, use_container_width=True)

# --- FILA 2: COMPRAS ---
st.header("2. Optimización de Compras (Minimizar)")
col3, col4 = st.columns(2)

with col3:
    df3 = cargar_datos('resultados3.csv')
    if df3 is not None:
        fig3 = px.bar(df3, x=df3.columns[0], y=df3.columns[1], 
                      title="Ej. 3: Compras sin límite (300€)",
                      color=df3.columns[1], color_continuous_scale=['#d3d3d3', '#1f77b4'])
        st.plotly_chart(fig3, use_container_width=True)

with col4:
    df4 = cargar_datos('resultados4.csv')
    if df4 is not None:
        fig4 = px.bar(df4, x=df4.columns[0], y=df4.columns[1], 
                      title="Ej. 4: Compras con Capacidad (360€)",
                      color=df4.columns[1], color_continuous_scale=['#d3d3d3', '#1f77b4'])
        st.plotly_chart(fig4, use_container_width=True)

# --- FILA 3: TRANSPORTE ---
st.header("3. Logística y Transporte")
df7 = cargar_datos('resultados7.csv')
if df7 is not None:
    # Creamos la etiqueta de la ruta
    df7['Ruta'] = df7['Almacen'] + ' ➔ ' + df7['Tienda']
    
    fig7 = px.bar(df7, x='Ruta', y='Unidades', 
                  title="Ej. 7: Rutas Óptimas de Transporte (Coste 1180€)",
                  color='Unidades', color_continuous_scale=['#d3d3d3', '#ff7f0e'])
    st.plotly_chart(fig7, use_container_width=True)
else:
    st.warning("Aún no se ha generado el archivo del Ejercicio 7.")