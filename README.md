# Maestrik

## Mongo Scripts

En esta carpeta se crea un script el cual recoge la información de un CSV(dataset) la procesa creando el esquema no relacional y lo sube con spark a una base de datos MongoDB almacenada en atlas

```
docker-compose up
```

## Jupyter Notebooks

Esta carpeta contiene los respectivos análisis exploratorios, entrenamientos y transformaciones de información necesarias para crear y procesar el dataset de forma que permita obtener 'insights'
- clusters_and_RFM_score: este notebook entrena los clusters de kmeans y GaussianMixture
- dataAnalisis: insights sobre dataset con clusters y RFM 
- SalesPrediction: análisis y forecasting usando sarimax(Seasonal Autoregressive Integrated Moving Average)

## Predict Service

Esta carpeta contiene un servicio de python3 con django el cual realiza predicciones y recomendaciones de compra basados en el tipo de usuario(subcluster y/o cluster) y/o actual item en carrito


ejecutar en el directorio ./predictService/Maestrik/
```
docker-compose up
```

para probar los request importar postman en el síguente archivo ./predictService/Maestrik/maestrik.postman_collection.json