import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import numbers

def LR(df: pd.DataFrame, x: str, y:str) -> None:

    fixedX = cambioVariable(df, x)
    model = sm.OLS(df[y], sm.add_constant(fixedX)).fit()
    print(model.summary())

    coef = pd.read_html(model.summary().tables[1].as_html(), header=0, index_col=0)[0]['coef']
    df.plot(x=x, y=y, kind='scatter')
    plt.plot(df_aux[x], [coef.values[1] + x + coef.values[0] for _, x in fixedX.items()], color='red')
    plt.xticks(rotation=90)
    plt.savefig('RegresionLineal_Publisher.png')
    plt.close()

def cambioVariable(df: pd.DataFrame, x: str) -> pd.Series:

    if isinstance(df[x][0], numbers.Number):

        return df[x]
    
    else:

        return pd.Series([i for i in range(0, len(df[x]))])

df = pd.read_csv('VJVentas.csv', nrows=5000)
df_aux = df.groupby("Publisher").agg({"Global_Sales": "sum"})
LR(df_aux, "Publisher", "Global_Sales")