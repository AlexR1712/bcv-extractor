#!/bin/env python
import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet

# Cargar los datos históricos de precios del Bitcoin
usd_data = pd.read_csv('datasetFINAL.csv')

# Preparar los datos para el modelo Prophet en venta
venta = usd_data.rename(columns={'Fecha': 'ds', 'Venta': 'y'})
venta['ds'] = pd.to_datetime(venta['ds'])

# Preparar los datos para el modelo Prophet en compra
compra = usd_data.rename(columns={'Fecha': 'ds', 'Compra': 'y'})
compra['ds'] = pd.to_datetime(compra['ds'])

# Crear y ajustar el modelo Prophet venta
model_venta = Prophet()
model_venta.fit(venta)

# Crear y ajustar el modelo Prophet compra
model_compra = Prophet()
model_compra.fit(compra)

# Crear un dataframe con las fechas futuras
future_dates_venta = model_venta.make_future_dataframe(periods=365)

# Crear un dataframe con las fechas futuras
future_dates_compra = model_compra.make_future_dataframe(periods=365)

# Realizar la predicción
forecast1 = model_venta.predict(future_dates_venta)
forecast2 = model_compra.predict(future_dates_compra)

forecast1.to_csv('PredictOutputventa.csv')
forecast2.to_csv('PredictOutputcompra.csv')

# Visualizar la predicción
model_venta.plot(forecast1, xlabel='Fecha', ylabel='Tasa Venta del USD/VES')
plt.title('Predicción de tasa Venta del USD / VES')
plt.show()

# Visualizar la predicción
model_compra.plot(forecast2, xlabel='Fecha', ylabel='Tasa Compra del USD/VES')
plt.title('Predicción de tasa Compra del USD / VES')
plt.show()

# Visualizar las tendencias y fluctuaciones en el precio
model_venta.plot_components(forecast1)
plt.show()


# Visualizar las tendencias y fluctuaciones en el precio
model_compra.plot_components(forecast2)
plt.show()