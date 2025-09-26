import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# ================================
# CONFIGURACIÓN DEL DASHBOARD
# ================================
st.set_page_config(page_title="Grupo 1 – Distribución de Edades de los Clientes",
                   layout="wide")

st.title("Grupo 1 – Distribución de Edades de los Clientes")
st.markdown("""
**Teoría y Fundamento del KPI:** La edad es un factor clave en marketing porque define segmentos de consumo.  
Un análisis de la distribución de edades nos permite identificar el público objetivo predominante y ajustar estrategias de comunicación.
""")

# ================================
# CARGA DE DATOS (¡LÍNEA CORREGIDA!)
# ================================
# Se asume que 'marketing_campaign.xlsx' está en el mismo directorio del repositorio
file_path = "marketing_campaign.xlsx"
df = pd.read_excel(file_path)

# ================================
# CREAR VARIABLES NECESARIAS
# ================================
# Edad calculada
df["Edad"] = 2025 - df["Year_Birth"]

# Gasto total
df["GastoTotal"] = (
    df["MntWines"] + df["MntFruits"] + df["MntMeatProducts"] +
    df["MntFishProducts"] + df["MntSweetProducts"] + df["MntGoldProds"]
)

# Estado civil
df["EstadoCivil"] = df["Marital_Status"]

# Género simulado (M/F) solo para fines prácticos
np.random.seed(42)  # reproducible
df["Genero"] = np.random.choice(["M", "F"], size=len(df))

# ================================
# LAYOUT DE COLUMNAS
# ================================
col1, col2 = st.columns([2, 1])

# ================================
# HISTOGRAMA PRINCIPAL
# ================================
with col1:
    st.subheader("Distribución de Edades")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(df["Edad"], bins=20, kde=False, color="skyblue", ax=ax)
    ax.set_xlabel("Edad")
    ax.set_ylabel("Número de clientes")
    st.pyplot(fig)

    # Rango de edad más frecuente
    counts = pd.cut(df["Edad"], bins=range(10, 100, 10)).value_counts().sort_values(ascending=False)
    rango_mayor = counts.index[0]
    st.markdown(f"📊 **El rango de edad más común es:** {rango_mayor}")

# ================================
# BOXLOT EDAD POR ESTADO CIVIL
# ================================
with col2:
    st.subheader("Edad según Estado Civil")
    fig, ax = plt.subplots(figsize=(5, 4))
    sns.boxplot(data=df, x="EstadoCivil", y="Edad", palette="Set2", ax=ax)
    st.pyplot(fig)

# ================================
# PROMEDIO DE GASTO POR RANGO DE EDAD
# ================================
st.subheader("Promedio de Gasto por Rango de Edad")
df["RangoEdad"] = pd.cut(df["Edad"], bins=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100], right=False)
gasto_por_rango = df.groupby("RangoEdad")["GastoTotal"].mean().reset_index()

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(data=gasto_por_rango, x="RangoEdad", y="GastoTotal", palette="coolwarm", ax=ax)
ax.set_ylabel("Promedio de Gasto")
st.pyplot(fig)

# ================================
# PIRÁMIDE DE POBLACIÓN
# ================================
st.subheader("Pirámide de Población (Edad vs Género)")
pop = df.groupby(["Edad", "Genero"]).size().unstack(fill_value=0)

# Negativos para hombres para graficar en pirámide
pop["M"] = -pop.get("M", 0)
pop["F"] = pop.get("F", 0)

fig, ax = plt.subplots(figsize=(8, 6))
ax.barh(pop.index, pop["M"], color="blue", label="Hombres")
ax.barh(pop.index, pop["F"], color="pink", label="Mujeres")
ax.set_xlabel("Cantidad de Clientes")
ax.set_ylabel("Edad")
ax.legend()
st.pyplot(fig)

# ================================
# STORYTELLING
# ================================
st.markdown("""
### 📈 Storytelling de Marketing
1. El rango de edad dominante marca el **público objetivo principal**.  
2. El boxplot revela cómo el **estado civil impacta en la edad promedio** de los clientes.  
3. El análisis de gasto muestra si los **jóvenes o adultos consumen más**.  
4. La pirámide poblacional permite diseñar campañas diferenciadas por género.  

👉 Esto ofrece un **mapa claro para orientar estrategias de marketing personalizadas**, optimizando recursos y maximizando impacto.
""")