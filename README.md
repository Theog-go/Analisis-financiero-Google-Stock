# 📊 Estudio Cuantitativo del Comportamiento Bursátil de Alphabet Inc.

Esta investigación examina las fluctuaciones del valor accionario de Alphabet Inc. (Google) mediante metodologías estadísticas avanzadas, incorporando análisis de series cronológicas y técnicas de predicción econométrica.

## 🎯 Propósito del Estudio

El presente trabajo busca desentrañar los patrones subyacentes en la cotización de las acciones de Google, empleando herramientas analíticas que permitan comprender la dinámica del mercado y generar proyecciones fundamentadas.

## 📋 Información del Dataset

**Origen:** Base de datos histórica en formato CSV conteniendo registros de cotizaciones bursátiles
**Variables incluidas:** Fecha, Apertura, Máximo, Mínimo, Cierre, Volumen operado
**Horizonte temporal:** Década 2015-2024

## 🔍 Metodología Aplicada

### Fase I: Preparación de la Información
- Tratamiento de observaciones ausentes mediante imputación por valor cero
- Conversión de variables temporales y establecimiento de índice cronológico
- Validación de integridad de los datos

### Fase II: Exploración Estadística
- Cálculo de medidas de tendencia central y dispersión
- Construcción de distribuciones de frecuencia para precios de cierre
- Análisis de asimetría y curtosis en las series

### Fase III: Análisis Relacional
- Desarrollo de matriz de covarianza entre variables precio-volumen
- Identificación de interdependencias significativas
- Evaluación de multicolinealidad

### Fase IV: Representación Visual
- Diagramas de dispersión para relación volumen-precio
- Gráficos de evolución temporal
- Mapas de calor para visualización de correlaciones

### Fase V: Creación de Indicadores
- **Rendimiento diario:** Variación porcentual inter-período
- **Volatilidad móvil:** Desviación estándar en ventana deslizante
- **Aproximación de margen:** Estimación de rentabilidad operativa

### Fase VI: Segmentación Temporal
- Análisis por cuartos de año para detectar estacionalidad
- Comparación de rendimientos por períodos específicos
- Identificación de ciclos recurrentes

### Fase VII: Modelización Predictiva
- Implementación de modelo ARIMA para pronóstico
- Validación cruzada y métricas de precisión
- Visualización de predicciones versus valores observados

## 📈 Descubrimientos Principales

- **Cohesión entre variables precio:** Existe una correlación robusta entre los diferentes indicadores de cotización
- **Independencia del volumen:** El volumen transaccional muestra baja capacidad predictiva sobre el precio final
- **Patrones estacionales:** Se detectan trimestres con rendimientos superiores, particularmente segundo y cuarto trimestre
- **Eficacia del modelo ARIMA:** La metodología logra capturar efectivamente la tendencia alcista sostenida

## 🛠️ Stack Tecnológico

**Lenguaje base:** Python 3.x
**Librerías principales:** 
- Pandas (manipulación de datos)
- Matplotlib/Seaborn (visualización)
- Statsmodels (análisis estadístico)
- NumPy (cálculos numéricos)

**Plataforma de desarrollo:** Jupyter Notebooks con integración Git

## 🔄 Instrucciones de Replicación

### Paso 1: Obtención del código
```bash
git clone https://github.com/Theog-go/Analisis-financiero-Google-Stock.git
cd Analisis-financiero-Google-Stock
```

### Paso 2: Configuración del entorno
```bash
pip install -r requirements.txt
```

### Paso 3: Ejecución del análisis
Abrir el archivo notebook (.ipynb) en Jupyter Lab o ejecutar el script Python directamente

## 👨‍💻 Información del Desarrollador

**Mateo García Ospina **
- Especialista en análisis cuantitativo y econometría financiera
- Enfoque en ciencia de datos aplicada a mercados bursátiles
- Proyecto desarrollado como parte de portafolio profesional

