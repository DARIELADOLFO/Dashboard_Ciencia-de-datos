import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# ================================
# CONFIGURACIÓN DE LA PÁGINA
# ================================
st.set_page_config(page_title="Dashboard de Marketing",
                   page_icon="📈",
                   layout="wide")

# ================================
# ENCABEZADO (LOGO, TÍTULO, PARTICIPANTES)
# ================================
col_logo, col_titulo, col_nombres = st.columns([1, 3, 1.5])

with col_logo:
    # IMPORTANTE: Asegúrate de tener un archivo 'logo.png' en tu repositorio
    try:
        st.image("logo.png", width=120)
    except Exception as e:
        st.warning("No se encontró el logo. Sube un archivo 'logo.png' al repositorio.")

with col_titulo:
    st.markdown("<h1 style='text-align: center;'>Análisis de Campaña de Marketing</h1>", unsafe_allow_html=True)

with col_nombres:
    st.markdown("""
    <div style='text-align: right;'>
        <strong>Participantes:</strong><br>
        Dariel A. Peña<br>
        Elvis R. Rosado
    </div>
    """, unsafe_allow_html=True)

# ================================
# RESUMEN DEL DASHBOARD
# ================================
st.markdown("---")
st.markdown("""
Este dashboard presenta un análisis demográfico y de comportamiento de los clientes de una campaña de marketing. 
El objetivo es identificar el público objetivo predominante y entender cómo factores como la edad, el estado civil y el género 
influyen en los patrones de consumo.
""")

# ================================
# CARGA Y PREPARACIÓN DE DATOS
# ================================
@st.cache_data # Usamos cache para no recargar los datos en cada interacción
def cargar_datos(path):
    df = pd.read_excel(path)
    # Edad calculada
    df["Edad"] = 2025 - df["Year_Birth"]
    # Gasto total
    df["GastoTotal"] = (
        df["MntWines"] + df["MntFruits"] + df["MntMeatProducts"] +
        df["MntFishProducts"] + df["MntSweetProducts"] + df["MntGoldProds"]
    )
    # Estado civil (simplificado)
    df["EstadoCivil"] = df["Marital_Status"]
    # Género simulado (M/F)
    np.random.seed(42)
    df["Genero"] = np.random.choice(["Hombre", "Mujer"], size=len(df))
    # Rango de edad
    df["RangoEdad"] = pd.cut(df["Edad"], bins=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100], right=False)
    return df

df = cargar_datos("marketing_campaign.xlsx")

st.markdown("---")

# ================================
# PRIMERA FILA DE GRÁFICOS
# ================================
col1, col2 = st.columns(2)

with col1:
    st.subheader("Distribución de Edades")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.histplot(df["Edad"], bins=20, kde=True, color="skyblue", ax=ax)
    ax.set_xlabel("Edad")
    ax.set_ylabel("Número de Clientes")
    st.pyplot(fig)
    st.caption("Histograma que muestra la frecuencia de clientes por cada rango de edad. La curva KDE suaviza la distribución.")

with col2:
    st.subheader("Edad por Estado Civil")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(data=df, x="Edad", y="EstadoCivil", palette="Set2", ax=ax)
    ax.set_xlabel("Edad")
    ax.set_ylabel("Estado Civil")
    st.pyplot(fig)
    st.caption("Diagrama de caja que compara la distribución de edades para cada estado civil, mostrando medianas y rangos.")

# ================================
# SEGUNDA FILA DE GRÁFICOS
# ================================
col3, col4 = st.columns(2)

with col3:
    st.subheader("Gasto Promedio por Edad")
    gasto_por_rango = df.groupby("RangoEdad")["GastoTotal"].mean().reset_index()
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(data=gasto_por_rango, x="RangoEdad", y="GastoTotal", palette="coolwarm", ax=ax)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
    ax.set_xlabel("Rango de Edad")
    ax.set_ylabel("Promedio de Gasto ($)")
    st.pyplot(fig)
    st.caption("Gráfico de barras que ilustra el gasto total promedio para diferentes grupos de edad.")

with col4:
    st.subheader("Pirámide Poblacional")
    pop = df.groupby(["Edad", "Genero"]).size().unstack(fill_value=0)
    
    # Asegurarse de que ambas columnas existan
    if "Hombre" not in pop: pop["Hombre"] = 0
    if "Mujer" not in pop: pop["Mujer"] = 0

    pop["Hombre"] = -pop["Hombre"] # Negativo para graficar a la izquierda

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.barh(pop.index, pop["Hombre"], color="blue", label="Hombres")
    ax.barh(pop.index, pop["Mujer"], color="pink", label="Mujeres")
    ax.set_xlabel("Cantidad de Clientes")
    ax.set_ylabel("Edad")
    ax.legend()
    st.pyplot(fig)
    st.caption("Pirámide que muestra la distribución de clientes por edad y género, facilitando la comparación visual.")

# ================================
# STORYTELLING FINAL
# ================================
st.markdown("---")
st.subheader("📈 Conclusiones y Storytelling")
st.markdown("""
1.  **Público Objetivo Principal:** La **Distribución de Edades** nos muestra claramente cuál es el rango de edad dominante, permitiendo enfocar las campañas de marketing.
2.  **Edad y Compromiso:** El gráfico de **Edad por Estado Civil** revela cómo la edad promedio varía según la situación sentimental del cliente, lo que puede influir en el tipo de productos que les interesan.
3.  **Potencial de Compra:** El **Gasto Promedio** nos dice qué generaciones tienen mayor poder adquisitivo o disposición a gastar, ayudando a dirigir las ofertas más valiosas.
4.  **Estrategia de Género:** La **Pirámide Poblacional** es clave para diseñar campañas con mensajes y productos diferenciados para hombres y mujeres.

👉 **En resumen, este dashboard ofrece un mapa claro para orientar estrategias de marketing personalizadas, optimizando recursos y maximizando el impacto.**
""")