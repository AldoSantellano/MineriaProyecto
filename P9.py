import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
import numbers
import pandas as pd
from tabulate import tabulate
from typing import Tuple, Dict
import numpy as np

df = pd.read_csv("VJVentas.csv")
cond1 = df["Publisher"] == 'Electronic Arts'
cond2 = df["Year"] > 1996
cond3 = df["Year"] < 2016
dfGroup = df.where(cond1 & cond2 & cond3)
db = dfGroup.groupby("Year").agg({"Global_Sales": "sum"})
db.reset_index(inplace=True)

model = smf.ols('Global_Sales ~ Year', db)
results = model.fit()
alpha = .05
predictions = results.get_prediction(db).summary_frame(alpha)


plt.scatter(db['Year'], db['Global_Sales'])
plt.plot(db['Year'], predictions['mean'], color='red')
plt.fill_between(db['Year'], predictions['obs_ci_lower'], predictions['obs_ci_upper'], alpha=.1)
plt.xlabel('Año')
plt.ylabel('Suma de Ventas Globales')

plt.show()
plt.close()