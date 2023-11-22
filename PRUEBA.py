import matplotlib.pyplot as plt
import statsmodels.api as sm
import numbers
import pandas as pd
import seaborn as sb
from tabulate import tabulate
from statsmodels.stats.outliers_influence import summary_table
from typing import Tuple, Dict
import numpy as np

db = pd.read_csv("VJVentas.csv", usecols=[1])
np.savetxt(r'D:\GitHub\MineriaProyecto\titulos.txt', db.values, fmt='%s')