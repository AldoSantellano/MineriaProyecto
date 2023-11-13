import csv
import pandas as pd
import requests
import io

def get_csv_from_url(url: str) -> pd.DataFrame:

    r = requests.get(url).content
    return pd.read_csv(io.StringIO(r.decode('utf-8')))

datos = []

def asignar_Instancias():

    data_total = []
    columnaObtenida = False

    with open('ventasVJ.csv', 'rt') as f:
        reader = csv.reader(f)
        for row in reader:

            if(columnaObtenida == False):
                data_total.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]])
                columnaObtenida = True
            else:
                data_total.append([row[0], row[1], row[2], row[3], row[4], row[5], float(row[6]) * 1000000, float(row[7]) * 1000000, float(row[8]) * 1000000,
                                   float(row[9]) * 1000000, float(row[10]) * 1000000])
    return(data_total)

datos = (asignar_Instancias())
df = pd.DataFrame(datos)
df.to_csv("VJVentas.csv", index=False, header=False)
df_filter = pd.read_csv('VJVentas.csv')
df_filter.dropna(subset=['Year', 'Publisher'], inplace=True)
df_filter.to_csv("VJVentas.csv", index=False, header=True)

#NOTA 13 DE NOV: Hice un cambio para borrar filas que no tengan info para
#arreglar unos problemas de practicas siguientes
