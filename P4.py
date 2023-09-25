import csv
import pandas as pd
import matplotlib.pyplot as plt

def Juegos100():
    #Código para obtener los géneros de los 100 juegos más vendidos en la historia
    df_v = df.groupby('Genre')['Genre'].value_counts()
    plot = df_v.plot.pie(y='Genre', figsize=(10,10), autopct="%1.0f%%")
    plt.savefig("100Juegos.png")
    plt.gcf().clear()

def Juegos100_Plataforma():
    #Código para obtener las plataformas en donde se encuentran los 100 juegos más vendidos en la historia
    df_p = df.groupby('Platform')['Platform'].value_counts()
    plot_p = df_p.plot.pie(y='Platform', figsize=(10,10), autopct="%1.0f%%")
    plt.savefig("100Juegos_Plataformas.png")
    plt.gcf().clear()

df = pd.read_csv('VJVentas.csv', nrows=100)
Juegos100()
Juegos100_Plataforma()



