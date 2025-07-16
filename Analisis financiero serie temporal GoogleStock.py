#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd

# Ruta completa del archivo
Googlepr = "C:/Users/theog/Downloads/GoogleStockPrices.csv" # <-- Ajusta a tu caso

# Leer el archivo CSV desde la ruta
df = pd.read_csv(Googlepr)

# Reemplazar todos los NaN por 0
df.fillna(0, inplace=True)

# Mostrar las primeras filas para verificar
print(df.head())


# In[7]:


# Ver estructura general
print(df.info())

# Estadísticas descriptivas
print(df.describe())

# Revisar valores únicos y nulos
print("\nValores nulos por columna:\n", df.isna().sum())
print("\nValores únicos por columna:\n", df.nunique())

# Convertir 'Date' a formato datetime (si aún no lo está)
df['Date'] = pd.to_datetime(df['Date'])

# Ver rango de fechas
print("\nRango de fechas:", df['Date'].min(), "→", df['Date'].max())



# In[8]:


import seaborn as sns
import matplotlib.pyplot as plt

# Calcular matriz de correlación
correlacion = df[['Open', 'High', 'Low', 'Close', 'Volume']].corr()

# Visualizar con mapa de calor
plt.figure(figsize=(8,6))
sns.heatmap(correlacion, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Matriz de correlación entre variables")
plt.show()


# In[9]:


# Histograma de precios de cierre
df['Close'].plot(kind='hist', bins=30, edgecolor='black', title='Distribución de precios de cierre')
plt.xlabel("Precio de Cierre")
plt.show()

# Relación entre volumen y precio de cierre
sns.scatterplot(data=df, x='Volume', y='Close')
plt.title("Relación entre Volumen y Precio de Cierre")
plt.show()


# In[10]:


# Retorno diario: porcentaje de cambio del precio de cierre
df['Return'] = df['Close'].pct_change()

# Volatilidad: desviación estándar móvil de 14 días del retorno
df['Volatility'] = df['Return'].rolling(window=14).std()

# Margen de utilidad: (Close - Open) / Open
df['Profit_Margin'] = (df['Close'] - df['Open']) / df['Open']


# In[11]:


print(df.info)


# In[12]:


print(df.head)


# In[13]:


# Crear columnas de año y trimestre
df['Year'] = df['Date'].dt.year
df['Quarter'] = df['Date'].dt.to_period('Q')

# Agrupar por trimestre y calcular promedio de retorno y margen
trimestral = df.groupby('Quarter').agg({
    'Return': 'mean',
    'Volatility': 'mean',
    'Profit_Margin': 'mean'
}).reset_index()

# Visualizar
import matplotlib.pyplot as plt
trimestral.set_index('Quarter')[['Return', 'Profit_Margin']].plot(kind='bar', figsize=(10,5))
plt.title("Rentabilidad y Margen por Trimestre")
plt.ylabel("Porcentaje Promedio")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()


# In[14]:


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Eliminar nulos (por rolling y pct_change)
df_model = df.dropna()

# Variables predictoras y objetivo
X = df_model[['Open', 'High', 'Low', 'Volume']]
y = df_model['Close']

# Dividir datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Predicciones
y_pred = modelo.predict(X_test)

# Evaluación
print("R2 Score:", r2_score(y_test, y_pred))
print("RMSE:", mean_squared_error(y_test, y_pred, squared=False))


# In[15]:


from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Asegúrate de tener un índice datetime
df_ts = df.set_index('Date')
df_ts = df_ts.asfreq('B')  # frecuencia diaria de negocio
df_ts['Close'] = df_ts['Close'].fillna(method='ffill')  # rellenar faltantes

# Crear modelo ARIMA simple
modelo_arima = ARIMA(df_ts['Close'], order=(5,1,0))  # puedes ajustar el orden
resultado = modelo_arima.fit()

# Predicción futura
pred = resultado.predict(start=len(df_ts)-30, end=len(df_ts)+30, typ='levels')

# Visualizar
df_ts['Close'].plot(label='Real', figsize=(10,5))
pred.plot(label='Predicción', color='red')
plt.title("Modelo ARIMA - Precio de Cierre")
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:




