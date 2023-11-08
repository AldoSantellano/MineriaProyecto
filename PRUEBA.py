import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import os
import numpy as np

db = pd.read_csv('VJVentas.csv', nrows=100)
db_g = db[["NA_Sales", "JP_Sales"]]

print(db_g)