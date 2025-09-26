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
    try:
        st.image("logo.png", width=120)
    except Exception as e:
        st.warning("Sube un archivo 'logo.png' al repositorio para mostrarlo.")

with col_titulo:
    st.markdown("<h1 style='text-align: center;'>Análisis de Campaña de Marketing</h1>", unsafe_allow_html=True)

with col_nombres:
    st.markdown("""
    <div style='text-align: right;'>
        <strong>Participantes:</strong><br>
        Dariel A. Peña<br>
        Elvis R. Rosado<br>
        Yaridis Terrero<br>
        Junior Padilla<br>
        Alfonso
    </div>
    """, unsafe_allow_html=True)

# ================================
# RESUMEN DEL DASHBOARD
# ================================
st.markdown("---")
st.markdown("""
Teoría y Fundamento del KPI: La edad es un factor clave en marketing porque define segmentos de consumo.<br>

Este dashboard presenta un análisis demográfico y de comportamiento de los clientes. 
*Usa los filtros en la barra lateral* para segmentar los datos y explorar los diferentes perfiles de consumidores.
""")

# CARGA Y PREPARACIÓN DE DATOS

@st.cache_data
def cargar_datos(path):
    df = pd.read_excel(path)
    df["Edad"] = 2025 - df["Year_Birth"]
    df["GastoTotal"] = (
        df["MntWines"] + df["MntFruits"] + df["MntMeatProducts"] +
        df["MntFishProducts"] + df["MntSweetProducts"] + df["MntGoldProds"]
    )
    df["EstadoCivil"] = df["Marital_Status"]
    np.random.seed(42)
    df["Genero"] = np.random.choice(["Hombre", "Mujer"], size=len(df))
    df["RangoEdad"] = pd.cut(df["Edad"], bins=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100], right=False)
    return df

df = cargar_datos("marketing_campaign.xlsx")


# BARRA LATERAL DE FILTROS (SIDEBAR)

st.sidebar.header("⚙️ Filtros de Segmentación")

# --- Filtro por Estado Civil ---
estados_civiles = sorted(df['EstadoCivil'].unique())
estado_civil_seleccionado = st.sidebar.multiselect(
    "Estado Civil",
    options=estados_civiles,
    default=estados_civiles
)

# --- Filtro por Rango de Edad (CORREGIDO) ---
rangos_edad_opciones = sorted(df['RangoEdad'].astype(str).unique())
rango_edad_seleccionado = st.sidebar.multiselect(
    "Rango de Edad",
    options=rangos_edad_opciones,
    default=rangos_edad_opciones
)

# --- Filtro por Género ---
generos = df['Genero'].unique()
genero_seleccionado = st.sidebar.multiselect(
    "Género",
    options=generos,
    default=generos
)

# --- Aplicar filtros al DataFrame (CORREGIDO) ---
df_filtrado = df[
    df['EstadoCivil'].isin(estado_civil_seleccionado) &
    df['RangoEdad'].astype(str).isin(rango_edad_seleccionado) & # <-- La corrección se aplica aquí
    df['Genero'].isin(genero_seleccionado)
]



# CUERPO PRINCIPAL DEL DASHBOARD

st.markdown("---")

if df_filtrado.empty:
    st.warning("⚠️ No hay datos disponibles para los filtros seleccionados. Por favor, amplía tu selección.")
else:
    # --- PRIMERA FILA DE GRÁFICOS ---
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Distribución de Edades")
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.histplot(df_filtrado["Edad"], bins=20, kde=True, color="skyblue", ax=ax)
        ax.set_xlabel("Edad")
        ax.set_ylabel("Número de Clientes")
        st.pyplot(fig)
        st.caption("Histograma de la frecuencia de clientes por edad para la selección actual.")

    with col2:
        st.subheader("Edad por Estado Civil")
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.boxplot(data=df_filtrado, x="Edad", y="EstadoCivil", palette="Set2", ax=ax)
        ax.set_xlabel("Edad")
        ax.set_ylabel("Estado Civil")
        st.pyplot(fig)
        st.caption("Distribución de edades para cada estado civil en el segmento filtrado.")

    # --- SEGUNDA FILA DE GRÁFICOS ---
    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Gasto Promedio por Edad")
        # Aseguramos que el groupby use la columna original para mantener el orden
        gasto_por_rango = df_filtrado.groupby("RangoEdad")["GastoTotal"].mean().reset_index()
        gasto_por_rango['RangoEdad'] = gasto_por_rango['RangoEdad'].astype(str) # Convertir a string para graficar
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.barplot(data=gasto_por_rango, x="RangoEdad", y="GastoTotal", palette="coolwarm", ax=ax)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
        ax.set_xlabel("Rango de Edad")
        ax.set_ylabel("Promedio de Gasto ($)")
        st.pyplot(fig)
        st.caption("Gasto total promedio para los diferentes grupos de edad seleccionados.")

    with col4:
        st.subheader("Pirámide Poblacional")
        pop = df_filtrado.groupby(["Edad", "Genero"]).size().unstack(fill_value=0)
        
        if "Hombre" not in pop: pop["Hombre"] = 0
        if "Mujer" not in pop: pop["Mujer"] = 0
        pop["Hombre"] = -pop["Hombre"]

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.barh(pop.index, pop["Hombre"], color="blue", label="Hombres")
        ax.barh(pop.index, pop["Mujer"], color="pink", label="Mujeres")
        ax.set_xlabel("Cantidad de Clientes")
        ax.set_ylabel("Edad")
        ax.legend()
        st.pyplot(fig)
        st.caption("Distribución de clientes por edad y género, según los filtros aplicados.")

    # --- STORYTELLING FINAL ---
    st.markdown("---")
    st.subheader("📈 Conclusiones y Storytelling")
    st.markdown("""
    1.  **Público Objetivo Principal:** La **Distribución de Edades** te muestra el rango de edad dominante del segmento que has filtrado.
    2.  **Edad y Compromiso:** El gráfico de **Edad por Estado Civil** revela cómo varía la edad promedio según la situación sentimental del cliente.
    3.  **Potencial de Compra:** El **Gasto Promedio** te dice qué generaciones de tu selección tienen mayor poder adquisitivo.
    4.  **Estrategia de Género:** La **Pirámide Poblacional** es clave para visualizar la composición de género del grupo seleccionado.

    👉 **Usa los filtros para descubrir insights específicos de cada segmento y tomar decisiones de marketing más informadas.**
    """)