import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sb
import numbers
from tabulate import tabulate
from sklearn.linear_model import LinearRegression
import pandas as pd


df = pd.read_csv('VJVentas.csv')
cond1 = df["Publisher"] == 'Electronic Arts'
cond2 = df["Year"] > 1996
cond3 = df["Year"] < 2016
dfGroup = df.where(cond1 & cond2 & cond3)

#Regresión Lineal de las ventas de EA globalmente. Mostrando si incrementan
#o lo contrario.
#sb.lmplot(x='Year', y='Global_Sales', data=dfGroup)
#plt.xlabel('Año')
#plt.ylabel('Ventas Totales (en millones)')
#plt.title('Regresión Lineal de Ventas de Videojuegos de EA')
#plt.show()
#plt.close()

db = dfGroup.groupby(["Year"]).agg({"Global_Sales": "sum"})
db.reset_index(inplace=True)

X = db['Year'].fillna(0).values.reshape(-1,1)
Y = db['Global_Sales'].fillna(0).values.reshape(-1,1)
lR = LinearRegression()
lR.fit(X,Y)
Y_Pred = lR.predict(X)

plt.scatter(X,Y)
plt.plot(X, Y_Pred, color='red')
plt.xlabel('Año')
plt.ylabel('Suma de Ventas Globales')
plt.show()


#NOTA 13 DE NOVIEMBRE: Noté que estaba algo fea la práctica. Así que la cambié!
#Debe seguir dando la misma información pero con mejor vista.