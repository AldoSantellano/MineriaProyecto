import matplotlib.pyplot as plt
import statsmodels.api as sm
import numbers
import pandas as pd
import seaborn as sb
from tabulate import tabulate
from statsmodels.stats.outliers_influence import summary_table
from typing import Tuple, Dict
import numpy as np


db = pd.read_csv('VJVentas.csv')
#db.dropna(subset=['Year', 'Publisher'], inplace=True)
#db.to_csv("VJVentas.csv", index=False, header=False)
print(db.isnull().sum())