#!/bin/env python
import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet

# Cargar los datos históricos de precios del Bitcoin
usd_data = pd.read_csv('datasetFINAL.csv')

# Preparar los datos para el modelo Prophet
usd_data = usd_data.rename(columns={'Fecha': 'ds', 'Venta': 'y'})
usd_data['ds'] = pd.to_datetime(usd_data['ds'])

# Crear y ajustar el modelo Prophet
model = Prophet()
model.fit(usd_data)

# Crear un dataframe con las fechas futuras
future_dates = model.make_future_dataframe(periods=365)

# Realizar la predicción
forecast = model.predict(future_dates)

# Visualizar la predicción
model.plot(forecast, xlabel='Fecha', ylabel='Tasa del USD/VES')
plt.title('Predicción de tasa del USD / VES')
plt.show()

# Visualizar las tendencias y fluctuaciones en el precio
model.plot_components(forecast)
plt.show()