# 📊 Dashboard de Marketing Estratégico

<div align="center">
  
  ![Dashboard Banner](https://img.shields.io/badge/Dashboard-Marketing%20Estratégico-blue?style=for-the-badge&logo=chart-line)
  ![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
  ![Streamlit](https://img.shields.io/badge/Streamlit-1.29.0-red?style=for-the-badge&logo=streamlit)
  ![Status](https://img.shields.io/badge/Status-Activo-green?style=for-the-badge)

  ### 🎯 Análisis de Campaña de Marketing con Insights Visuales Interactivos

  *Desarrollado por el Equipo de Análisis de Datos*

</div>

---

## 📝 Introducción

El **Dashboard de Marketing Estratégico** es una aplicación web interactiva diseñada para analizar y visualizar datos de campañas de marketing, proporcionando insights valiosos sobre segmentación demográfica, patrones de consumo y métricas clave de clientes.

Esta herramienta utiliza técnicas avanzadas de visualización de datos para transformar información compleja en insights accionables, permitiendo a los equipos de marketing tomar decisiones estratégicas basadas en datos reales.

### 🎯 Temática Principal: Segmentación por KPIs Demográficos

La aplicación se centra en la **teoría del KPI de segmentación por edad**, donde la edad actúa como un factor determinante en:

- 💰 **Patrones de consumo**
- 🛒 **Poder adquisitivo**  
- ❤️ **Preferencias de producto**
- 🎯 **Comportamiento de compra**

---

## ✨ Características Principales

### 📊 **Visualizaciones Detalladas**

El dashboard incluye múltiples tipos de análisis visual:

#### **📈 Gráficos de Segmentación Demográfica**
- **Histograma de Edades**: Distribución de frecuencia de clientes por edad
- **Box Plot por Estado Civil**: Variación de edades según estado marital
- **Pirámide Poblacional**: Distribución por género y edad
- **Gráfico Circular de Género**: Proporción de clientes por género

#### **💰 Análisis de Comportamiento de Compra**
- **Gasto por Rango de Edad**: Poder adquisitivo por segmento etario
- **Distribución de Gasto por Categoría**: Análisis detallado de 6 categorías:
  - 🍷 Vinos (`MntWines`)
  - 🍎 Frutas (`MntFruits`)  
  - 🥩 Productos cárnicos (`MntMeatProducts`)
  - 🐟 Productos pesqueros (`MntFishProducts`)
  - 🍰 Productos dulces (`MntSweetProducts`)
  - 👑 Productos premium (`MntGoldProds`)

#### **🛒 Análisis de Canales de Venta**
- **Compras por Canal**: Comparación de 4 canales principales:
  - 🎁 Ofertas/Descuentos (`NumDealsPurchases`)
  - 🌐 Sitio web (`NumWebPurchases`)
  - 📚 Catálogo (`NumCatalogPurchases`)
  - 🏪 Tienda física (`NumStorePurchases`)

#### **🎯 Efectividad de Campañas de Marketing**
- **Participación en Campañas**: Análisis de 6 campañas:
  - Campañas 1-5 (`AcceptedCmp1` a `AcceptedCmp5`)
  - Respuesta general (`Response`)
- **Tendencia de Compras**: Visualización temporal (datos simulados para demostración)

#### **🏆 Análisis de Clientes Premium**
- **Tabla de Top Clientes**: Los 10 clientes con mayor gasto total
- **Formato condicional** con indicadores de satisfacción visuales
- **Métricas combinadas**: Edad, género, estado civil, gasto total e ingresos

### 🔧 **Filtros Dinámicos**
- 💍 Filtro por estado civil (multiselección)
- 🎂 Filtro por rango de edad
- ♂️♀️ Filtro por género
- 🔄 Actualización en tiempo real

### 📊 **Métricas Clave**
- 👥 Total de clientes segmentados
- 💰 Gasto promedio del segmento
- 🎂 Edad promedio
- 👤 Género dominante

### 🧠 **Insights Estratégicos**
- 🎯 Identificación de público objetivo
- 💡 Recomendaciones personalizadas
- 📈 Análisis de potencial de compra
- 🎪 Estrategias de segmentación

---

## 🛠️ Tecnologías Utilizadas

### 🐍 **Backend & Procesamiento**
- ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) **Python 3.8+** - Lenguaje principal
- ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white) **Pandas 2.2.1** - Manipulación de datos
- ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white) **NumPy 1.26.0** - Cálculos numéricos

### 🎨 **Frontend & Visualización**
- ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white) **Streamlit 1.29.0** - Framework web
- ![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat&logo=plotly&logoColor=white) **Plotly 5.18.0** - Gráficos interactivos
- ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat&logo=matplotlib&logoColor=white) **Matplotlib 3.8.0** - Visualización básica
- ![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=flat&logo=seaborn&logoColor=white) **Seaborn 0.13.2** - Estadísticas visuales

### 📁 **Manejo de Archivos**
- ![Excel](https://img.shields.io/badge/Excel-217346?style=flat&logo=microsoft-excel&logoColor=white) **OpenPyXL 3.1.2** - Lectura de archivos Excel

---

## 📦 Instalación y Configuración

### 📋 **Requisitos del Sistema**

| Componente | Especificación |
|------------|----------------|
| 💻 **Sistema Operativo** | Windows 10/11, macOS 10.14+, Linux |
| 🐍 **Python** | 3.8+ (Recomendado: 3.9-3.11) |
| 🧠 **RAM** | 4GB mínimo (8GB+ recomendado) |
| 💾 **Espacio en Disco** | 500MB |
| ⚡ **Procesador** | Dual-core 2GHz+ |

### 🚀 **Instalación Paso a Paso**

#### **1️⃣ Preparar el Entorno**

```bash
# Crear entorno virtual
python -m venv dashboard_env

# Activar entorno virtual
# Windows:
dashboard_env\Scripts\activate
# macOS/Linux:
source dashboard_env/bin/activate

# Actualizar pip
python -m pip install --upgrade pip
```

#### **2️⃣ Instalar Dependencias**

```bash
# Opción 1: Desde requirements.txt
pip install -r requirements.txt

# Opción 2: Instalación manual
pip install streamlit==1.29.0 pandas==2.2.1 matplotlib==3.8.0 seaborn==0.13.2 numpy==1.26.0 openpyxl==3.1.2 plotly==5.18.0
```

#### **3️⃣ Preparar Datos**

Asegúrate de tener el archivo `marketing_campaign.xlsx` con las siguientes columnas:

| Columna | Descripción | Tipo |
|---------|-------------|------|
| `Year_Birth` | 📅 Año de nacimiento | Integer |
| `Marital_Status` | 💍 Estado civil | String |
| `Income` | 💰 Ingreso del cliente | Float |
| `Education` | 🎓 Nivel educativo | String |
| `Dt_Customer` | 📆 Fecha registro cliente | Date |
| `Recency` | 🔄 Días desde última compra | Integer |

#### **🛍️ Columnas de Gastos por Categoría**
| Columna | Descripción | Tipo |
|---------|-------------|------|
| `MntWines` | 🍷 Gasto en vinos | Float |
| `MntFruits` | 🍎 Gasto en frutas | Float |
| `MntMeatProducts` | 🥩 Gasto en carnes | Float |
| `MntFishProducts` | 🐟 Gasto en pescados | Float |
| `MntSweetProducts` | 🍰 Gasto en dulces | Float |
| `MntGoldProds` | 👑 Gasto en productos premium | Float |

#### **🛒 Columnas de Compras por Canal**
| Columna | Descripción | Tipo |
|---------|-------------|------|
| `NumDealsPurchases` | 🎁 Compras con ofertas/descuentos | Integer |
| `NumWebPurchases` | 🌐 Compras vía página web | Integer |
| `NumCatalogPurchases` | 📚 Compras vía catálogo | Integer |
| `NumStorePurchases` | 🏪 Compras en tienda física | Integer |
| `NumWebVisitsMonth` | 👀 Visitas web mensuales | Integer |

#### **🎯 Columnas de Participación en Campañas**
| Columna | Descripción | Tipo |
|---------|-------------|------|
| `AcceptedCmp1` | ✅ Aceptó campaña 1 (0/1) | Integer |
| `AcceptedCmp2` | ✅ Aceptó campaña 2 (0/1) | Integer |
| `AcceptedCmp3` | ✅ Aceptó campaña 3 (0/1) | Integer |
| `AcceptedCmp4` | ✅ Aceptó campaña 4 (0/1) | Integer |
| `AcceptedCmp5` | ✅ Aceptó campaña 5 (0/1) | Integer |
| `Response` | 📩 Respuesta última campaña (0/1) | Integer |
| `Complain` | 😞 Cliente realizó quejas (0/1) | Integer |

#### **📈 Columnas Adicionales**
| Columna | Descripción | Tipo |
|---------|-------------|------|
| `Kidhome` | 👶 Número de niños pequeños | Integer |
| `Teenhome` | 👦 Número de adolescentes | Integer |
| `Z_CostContact` | 💸 Costo de contacto | Float |
| `Z_Revenue` | 💵 Revenue generado | Float |

#### **4️⃣ Ejecutar la Aplicación**

```bash
# Navegar al directorio del proyecto
cd /ruta/al/directorio/del/proyecto

# Ejecutar Streamlit
streamlit run Pactica_Ddashboard.py

# La aplicación se abrirá en: http://localhost:8501
```

---

## 📁 Estructura del Proyecto

```
📂 proyecto_dashboard/
├── 📄 Pactica_Ddashboard.py    # 🚀 Aplicación principal
├── 📄 requirements.txt         # 📦 Dependencias
├── 📊 marketing_campaign.xlsx  # 📈 Datos de entrada
├── 🖼️ logo.png                # 🎨 Logo del proyecto
├── 📚 README.md               # 📖 Documentación
└── 📁 assets/                 # 🎨 Recursos adicionales
    ├── 🎨 screenshots/        # 📸 Capturas de pantalla
    └── 📄 docs/              # 📚 Documentación extra
```

---

## 🎮 Guía de Uso

### 🎯 **Navegación Principal**

1. **🔧 Panel de Filtros (Sidebar)**
   - 💍 Selecciona estado civil
   - 🎂 Elige rangos de edad
   - ♂️♀️ Filtra por género

2. **📊 Métricas Principales**
   - 👥 Clientes segmentados
   - 💰 Gasto promedio
   - 🎂 Edad promedio
   - 👤 Género dominante

3. **📈 Visualizaciones Interactivas**
   - Haz clic en elementos para más información
   - Usa zoom y pan en los gráficos
   - Hover para detalles específicos

### 🎪 **Funcionalidades Avanzadas**

#### **🔍 Segmentación Inteligente**
- Combina múltiples filtros para análisis específicos
- Obtén insights en tiempo real
- Exporta datos filtrados

#### **📊 Análisis Comparativo**
- Compara diferentes segmentos
- Identifica tendencias y patrones
- Visualiza correlaciones

#### **💡 Insights Automáticos**
- Recomendaciones estratégicas
- Identificación de público objetivo
- Análisis de potencial de mercado

---

## 🎨 Interfaz de Usuario

### 🌃 **Tema Oscuro Moderno**
- 🎨 Paleta de colores GitHub Dark
- ✨ Gradientes y sombras suaves
- 🔤 Tipografía Inter optimizada
- 📱 Diseño responsivo

### 🎭 **Componentes Visuales**

| Componente | Descripción | Estilo |
|------------|-------------|--------|
| 📊 **Métricas** | Cards con gradientes y bordes | Dark theme + Blue accents |
| 📈 **Gráficos** | Plotly interactivos | Colores consistentes |
| 🔘 **Botones** | Hover effects y transiciones | GitHub blue theme |
| 📋 **Filtros** | Multi-select con emojis | Sidebar organizada |

---

## 🔧 Solución de Problemas

### ❌ **Errores Comunes**

#### **📁 Archivo No Encontrado**
```bash
❌ Error: FileNotFoundError: 'marketing_campaign.xlsx'

✅ Solución:
- Verifica que el archivo esté en el directorio correcto
- Confirma el nombre exacto del archivo
- Revisa permisos de lectura
```

#### **📦 Dependencias Faltantes**
```bash
❌ Error: ModuleNotFoundError

✅ Solución:
- Activa el entorno virtual
- Reinstala: pip install -r requirements.txt
- Verifica la versión de Python
```

#### **🌐 Puerto Ocupado**
```bash
❌ Error: Puerto 8501 ocupado

✅ Solución:
- Cambiar puerto: streamlit run app.py --server.port 8502
- Cerrar otras instancias de Streamlit
```

### 📞 **Soporte Técnico**

Si encuentras problemas:

1. 📝 **Reporta el Error**
   - Incluye versión de Python
   - Mensaje de error completo
   - Sistema operativo y versión

2. 💬 **Contacto**
   - Crea un issue en el repositorio
   - Incluye capturas de pantalla
   - Describe los pasos para reproducir

---

## 👥 Equipo de Desarrollo

<div align="center">

### 🚀 **Desarrolladores Principales**

| 👤 Nombre | 🎯 Rol | 💼 Especialidad |
|-----------|---------|-----------------|
| **Dariel A. Peña** | 🔧 Lead Developer | Backend & Data Processing |
| **Elvis R. Rosado** | 🎨 UI/UX Developer | Frontend & Visualizations |
| **Yaridis Terrero** | 📊 Data Analyst | Statistics & Insights |
| **Junior Padilla** | 🧪 QA Engineer | Testing & Optimization |
| **Alfonso** | 📚 Tech Writer | Documentation & Support |

</div>

---

## 📊 Interpretación de Resultados

### 🎯 **Métricas Clave Explicadas**

#### **👥 Clientes Segmentados**
- **Definición**: Total de clientes que cumplen con los filtros aplicados
- **Uso**: Evalúa el tamaño del segmento objetivo
- **Benchmark**: Compara con el total de la base de datos

#### **💰 Gasto Promedio**
- **Definición**: Media del gasto total de los clientes filtrados
- **Uso**: Identifica el valor del cliente promedio
- **Insight**: Segmentos con mayor gasto = mayor valor

#### **🎂 Edad Promedio**
- **Definición**: Media de la edad de los clientes filtrados
- **Uso**: Caracteriza demográficamente el segmento
- **Estrategia**: Adapta mensajes según grupo etario

#### **👤 Género Dominante**
- **Definición**: Categoría de género más común en el segmento
- **Uso**: Orienta el enfoque de comunicación
- **Aplicación**: Personaliza campañas por género

### 📈 **Interpretación de Gráficos**

### 📊 **Interpretación Avanzada de Visualizaciones**

#### **🛍️ Distribución de Gasto por Categoría**
```
Datos utilizados:
✅ MntWines - Gasto promedio en vinos
✅ MntFruits - Gasto promedio en frutas  
✅ MntMeatProducts - Gasto promedio en carnes
✅ MntFishProducts - Gasto promedio en pescados
✅ MntSweetProducts - Gasto promedio en dulces
✅ MntGoldProds - Gasto promedio en productos premium

Interpretación estratégica:
• Barras altas = Categorías de mayor inversión
• Comparación relativa entre categorías
• Identificación de oportunidades de cross-selling
```

#### **🛒 Compras por Canal de Venta**
```
Datos utilizados:
✅ NumDealsPurchases - Compras con ofertas/descuentos
✅ NumWebPurchases - Compras vía web
✅ NumCatalogPurchases - Compras por catálogo
✅ NumStorePurchases - Compras en tienda física

Insights estratégicos:
• Canal dominante = Mayor inversión de recursos
• Canales débiles = Oportunidades de mejora
• Estrategia omnicanal personalizada
```

#### **🎯 Participación en Campañas**
```
Datos utilizados:
✅ AcceptedCmp1 - Tasa de aceptación campaña 1
✅ AcceptedCmp2 - Tasa de aceptación campaña 2
✅ AcceptedCmp3 - Tasa de aceptación campaña 3
✅ AcceptedCmp4 - Tasa de aceptación campaña 4
✅ AcceptedCmp5 - Tasa de aceptación campaña 5
✅ Response - Respuesta a última campaña

Análisis de efectividad:
• Valores 0-1 convertidos a porcentajes
• Campañas exitosas = Mayor tasa de respuesta
• Patrones de comportamiento del cliente
```

#### **📅 Tendencia de Compras (Simulada)**
```
⚠️ IMPORTANTE: Este gráfico usa datos simulados
• NO refleja información del archivo Excel
• Propósito: Demostración de capacidades visuales
• En implementación real: usar datos temporales reales
```

#### **🏆 Tabla Top Clientes**
```
Datos combinados:
✅ Edad calculada (2025 - Year_Birth)
✅ Género (simulado para demostración)
✅ EstadoCivil (Marital_Status)
✅ GastoTotal (suma de todas las categorías MntX)
✅ Income (ingresos del cliente)

Formato condicional:
😊 Excelente - Gasto > percentil 75
😐 Regular - Gasto entre percentil 25-75  
😔 Bajo - Gasto < percentil 25
```

---

## 🔒 Seguridad y Privacidad

### 🛡️ **Protección de Datos**

- ✅ **Procesamiento Local**: Todos los cálculos se realizan localmente
- ✅ **Sin Transmisión**: Los datos no se envían a servidores externos
- ✅ **Acceso Controlado**: Aplicación ejecuta solo en puerto local
- ✅ **Sin Almacenamiento**: No se guardan datos personales

### 🔐 **Medidas de Seguridad**

| Aspecto | Medida Implementada |
|---------|-------------------|
| 📁 **Datos** | Permanecen en sistema local |
| 🌐 **Red** | Puerto local no expuesto |
| 🔒 **Acceso** | Sin autenticación externa requerida |
| 💾 **Almacenamiento** | Sin persistencia de datos personales |

---

## 📚 Recursos Adicionales

### 📖 **Documentación Oficial**

| Tecnología | Enlace | Descripción |
|------------|--------|-------------|
| 🌊 **Streamlit** | [docs.streamlit.io](https://docs.streamlit.io) | Framework web para aplicaciones de datos |
| 🐼 **Pandas** | [pandas.pydata.org](https://pandas.pydata.org/docs/) | Manipulación y análisis de datos |
| 📊 **Plotly** | [plotly.com/python](https://plotly.com/python/) | Visualización interactiva |
| 🧮 **NumPy** | [numpy.org](https://numpy.org/doc/) | Cálculos científicos |

### 🎓 **Tutoriales Recomendados**

- 📘 [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
- 🎨 [Streamlit Components Gallery](https://streamlit.io/components)
- 📊 [Plotly Tutorial Series](https://plotly.com/python/basic-charts/)
- 🔬 [Data Analysis with Pandas](https://pandas.pydata.org/docs/getting_started/intro_tutorials/)

### 💡 **Ejemplos de Uso Avanzado**

```python
# Ejemplo: Análisis personalizado
segmento_vip = df_filtrado[df_filtrado['GastoTotal'] > df_filtrado['GastoTotal'].quantile(0.8)]
insight_vip = f"Clientes VIP: {len(segmento_vip)} ({len(segmento_vip)/len(df_filtrado)*100:.1f}%)"
```

---

## 🚀 Roadmap y Futuras Mejoras

### 📅 **Versión 1.3.0** (Próximamente)
- 🤖 **Machine Learning**: Predicciones de comportamiento usando scikit-learn
- 📈 **Análisis Temporal Real**: Integración con datos de `Dt_Customer` para tendencias temporales
- 📊 **Dashboard de Quejas**: Análisis detallado de la columna `Complain`
- 🏠 **Segmentación Familiar**: Análisis basado en `Kidhome` y `Teenhome`
- 📱 **Análisis de Engagement Web**: Métricas basadas en `NumWebVisitsMonth`

### 📅 **Versión 1.4.0** (En Planificación)
- 💰 **ROI por Campaña**: Análisis de `Z_Revenue` vs `Z_CostContact`
- 📊 **Correlaciones Avanzadas**: Matriz de correlación entre todas las variables
- 🎓 **Segmentación Educativa**: Análisis por nivel de `Education`
- 🌐 **Dashboard Responsivo**: Optimización móvil completa
- 📧 **Reportes Automatizados**: Envío de insights programados

### 💭 **Ideas Futuras**
- 🔗 **API de CRM**: Integración con sistemas externos
- 🧠 **IA Predictiva**: Modelos de Customer Lifetime Value (CLV)
- 📊 **Análisis de Cohortes**: Seguimiento longitudinal de clientes
- 🎯 **A/B Testing**: Comparación de efectividad de campañas
- 📱 **App Móvil**: Dashboard nativo para dispositivos móviles

---

## 📄 Licencia y Términos

### 📝 **Licencia de Uso**

Este proyecto está desarrollado con fines **educativos y de demostración**. 

```
📋 TÉRMINOS DE USO:
✅ Uso educativo y académico
✅ Modificación y personalización
✅ Distribución con atribución
❌ Uso comercial sin autorización
❌ Redistribución sin créditos
```

### 👨‍💻 **Créditos y Atribución**

**Desarrollado por:**
- 🎯 **Equipo de Análisis de Datos**
- 📧 **Contacto**: [Información de contacto del equipo]
- 🌐 **Repositorio**: [URL del repositorio]

---

## 📞 Contacto y Soporte

### 🆘 **Soporte Técnico**

¿Necesitas ayuda? Contáctanos:

📧 **Email**: soporte.dashboard@equipo.com  
💬 **Issues**: [GitHub Issues](https://github.com/tu-repo/issues)  
📚 **Wiki**: [Documentación Extendida](https://github.com/tu-repo/wiki)  

### 📊 **Reportes y Feedback**

Tu feedback es importante:

- ⭐ **Valoración**: Deja una estrella en GitHub
- 🐛 **Bug Reports**: Reporta errores encontrados  
- 💡 **Sugerencias**: Propón nuevas características
- 📈 **Casos de Uso**: Comparte cómo usas el dashboard

---

## 📈 Estadísticas del Proyecto

<div align="center">

![GitHub stars](https://img.shields.io/github/stars/usuario/proyecto?style=social)
![GitHub forks](https://img.shields.io/github/forks/usuario/proyecto?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/usuario/proyecto?style=social)

![GitHub last commit](https://img.shields.io/github/last-commit/usuario/proyecto)
![GitHub repo size](https://img.shields.io/github/repo-size/usuario/proyecto)
![Lines of code](https://img.shields.io/tokei/lines/github/usuario/proyecto)

</div>

---

<div align="center">

### 🎯 ¡Gracias por usar nuestro Dashboard de Marketing Estratégico! 

**Si te resulta útil, no olvides darle una ⭐ al proyecto**

---

📊 **Hecho con** ❤️ **por el Equipo de Análisis de Datos**  
🚀 **Potenciado por** Python, Streamlit y Plotly  
🎯 **Enfocado en** Insights Accionables y Decisiones Basadas en Datos

</div>
