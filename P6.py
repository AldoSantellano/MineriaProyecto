import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sb
import numbers
import pandas as pd


dataset = pd.read_csv('VJVentas.csv')
dataGroup = dataset.where(dataset["Publisher"] == 'Electronic Arts')

#Regresión Lineal de las ventas de EA globalmente. Mostrando si incrementan
#o lo contrario.
sb.lmplot(x='Year', y='Global_Sales', data=dataGroup)
plt.xlabel('Año')
plt.ylabel('Ventas Totales (en millones)')
plt.title('Regresión Lineal de Ventas de Videojuegos de EA')
plt.show()
plt.close()