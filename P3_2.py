import csv
import pandas as pd
import requests
import io

#Para cada plataforma de videojuegos, su juego con menor, mayor ventas. Y la suma de ventas totales.

df = pd.read_csv('VJVentas.csv')
result = df.groupby('Platform')['Global_Sales'].agg(['min','max','sum'])
tabla = pd.DataFrame(result)
result.to_csv("VentasPlataforma.csv")
print(result)