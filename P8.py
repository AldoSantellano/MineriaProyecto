import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import os
import numpy as np

db = pd.read_csv('VJVentas.csv', nrows=100, skiprows=[1])
df = db[["NA_Sales", "EU_Sales"]]

for k in range(1,8):
    kmeans = KMeans(n_clusters=k, random_state=0, n_init=5)
    kmeans.fit_predict(df)
    plt.scatter(x=df["NA_Sales"], y=df["EU_Sales"], c=kmeans.labels_)
    plt.xlabel('Ventas en Norte América')
    plt.ylabel('Ventas en Europa')
    plt.savefig(os.path.join('Practica8PLOTS', 'K ='+str(k)))
    plt.clf()
