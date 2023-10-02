import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

def anova():

    df_aux = df.groupby(["Publisher", "Year"]).agg({"Global_Sales": "sum"})
    df_aux.reset_index(inplace=True)
    anova_Calculo(df_aux, "Global_Sales ~ Year + Publisher")
    

def anova_Calculo(df_aux: pd.DataFrame, str_ols: str):

    modl = ols(str_ols, data=df_aux).fit()
    anova_df = sm.stats.anova_lm(modl, typ=2)

    if anova_df["PR(>F)"][0] < 0.005:

        print("Hay diferencias significativas.")
        print(anova_df)
    else:
        
        print("No hay diferencias significativas.")

# Sacar el ANOVA de cada Publisher por año, para los 5000 juegos más vendidos. Así determinar si cada publisher tiene el mismo éxito en sus juegos.
df = pd.read_csv('VJVentas.csv', nrows=5000)
anova()
