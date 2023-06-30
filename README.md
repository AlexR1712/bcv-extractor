# Proyecto BCV-Forecasting
Este proyecto contiene el código fuente necesario para hacer scrapping al sitio web del Banco Central de Venezuela (BCV) y obtener las tasas de compra y venta de divisas. El objetivo principal es realizar un forecasting del par VES/USD utilizando el paquete Prophet de Meta.

Archivos principales
El proyecto consta de tres archivos principales:

1. bcv_scrapper.py: Este archivo contiene el código necesario para hacer scrapping de la web del BCV y descargar los archivos de Excel con las tasas de cambio.

2. extract_xls_data.py: Este archivo se encarga de procesar los archivos de Excel descargados durante el scrapping y extraer las tasas de cambio del par VES/USD.

3. forecasting.py: En este archivo se hace uso del paquete Prophet de Meta para realizar el forecasting respectivo del par VES/USD.

# Cómo funciona Prophet
Prophet es un paquete desarrollado por Meta para realizar predicciones en series temporales. Está basado en un modelo aditivo, donde las tendencias no lineales se ajustan a la estacionalidad anual, semanal y diaria, así como a los efectos de los días festivos.

Este paquete utiliza la técnica de regresión de componentes aditivos generalizados (GAM) y el algoritmo de optimización L-BFGS para realizar el fitting del modelo. Además, Prophet es capaz de manejar datos faltantes y cambios en las tendencias, lo que lo hace ideal para trabajar con series temporales complejas.

# Requisitos
Para ejecutar este proyecto, asegúrese de tener instaladas las siguientes dependencias:

- Python 3.7 o superior
- pandas
- requests
- BeautifulSoup4
- openpyxl
- prophet

Puede instalar las dependencias utilizando el siguiente comando:

```bash

pip install -r requirements.txt

```

# Uso
Para utilizar este proyecto, siga los siguientes pasos:

1. Ejecute el scrapper para descargar los archivos de Excel con las tasas de cambio:

```bash

python bcv_scrapper.py

```

2. Procese los archivos de Excel descargados para extraer las tasas de cambio del par VES/USD:

```bash

python extract_xls_data.py

```

3. Realice el forecasting del par VES/USD:

```bash

python forecasting.py

```

Los resultados del forecasting se guardarán en un archivo CSV y se generará un gráfico con las predicciones.


# Licencia
Este proyecto se distribuye bajo la licencia MIT. Consulte el archivo LICENSE para obtener más información.