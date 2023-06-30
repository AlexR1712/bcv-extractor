#!/bin/env python
import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet


def main():
    # Cargar los datos históricos de precios del BCV
    try:
        usd_data = pd.read_csv('datasetFINAL.csv')
    except FileNotFoundError:
        print("Error: Archivo datasetFINAL.csv no encontrado.")
        return

    # Preparar los datos para el modelo Prophet en venta
    venta_data = usd_data.rename(columns={'Fecha': 'ds', 'Venta': 'y'})
    venta_data['ds'] = pd.to_datetime(venta_data['ds'])

    # Preparar los datos para el modelo Prophet en compra
    compra_data = usd_data.rename(columns={'Fecha': 'ds', 'Compra': 'y'})
    compra_data['ds'] = pd.to_datetime(compra_data['ds'])

    # Crear y ajustar el modelo Prophet venta
    model_venta = Prophet()
    model_venta.fit(venta_data)

    # Crear y ajustar el modelo Prophet compra
    model_compra = Prophet()
    model_compra.fit(compra_data)

    # Crear un dataframe con las fechas futuras
    future_dates_venta = model_venta.make_future_dataframe(periods=365)

    # Crear un dataframe con las fechas futuras
    future_dates_compra = model_compra.make_future_dataframe(periods=365)

    # Realizar la predicción
    forecast1 = model_venta.predict(future_dates_venta)
    forecast2 = model_compra.predict(future_dates_compra)

    # Guardar las predicciones en archivos CSV
    with open('PredictOutputventa.csv', 'w') as f:
        forecast1.to_csv(f, index=False)
    with open('PredictOutputcompra.csv', 'w') as f:
        forecast2.to_csv(f, index=False)

    # Visualizar la predicción de venta
    model_venta.plot(forecast1, xlabel='Fecha', ylabel='Tasa Venta del USD/VES')
    plt.title('Predicción de tasa Venta del USD / VES')
    plt.savefig('prediccion_venta.png')
    plt.show()

    # Visualizar la predicción de compra
    model_compra.plot(forecast2, xlabel='Fecha', ylabel='Tasa Compra del USD/VES')
    plt.title('Predicción de tasa Compra del USD / VES')
    plt.savefig('prediccion_compra.png')
    plt.show()

    # Visualizar las tendencias y fluctuaciones en el precio de venta
    model_venta.plot_components(forecast1)
    plt.savefig('tendencias_venta.png')
    plt.show()

    # Visualizar las tendencias y fluctuaciones en el precio de compra
    model_compra.plot_components(forecast2)
    plt.savefig('tendencias_compra.png')
    plt.show()


if __name__ == "__main__":
    main()