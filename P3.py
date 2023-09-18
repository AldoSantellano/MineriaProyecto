import csv
import pandas as pd
import requests
import io

def leer_Genero():
    result = df.groupby('Genre')['Global_Sales'].sum()
    print(result)

def leer_GeneroEnJapon():
    result = df.groupby('Genre')['JP_Sales'].sum()
    print(result)

def leer_VentasMayoresPorGenero():
    result = df.groupby('Genre')['Global_Sales'].max()
    print(result)

def leer_MayorJuegoPorAnio():
    result = df.groupby('Year')['Global_Sales'].max()
    print(result)

def leer_MayorVentaPorPlataforma():
    result = df.groupby('Platform')['Global_Sales'].max()
    print(result)
    

df = pd.read_csv('VJVentas.csv')

#Cambiar la función de abajo para usar las otras funciones y ver otros tipos de datos
leer_MayorVentaPorPlataforma()