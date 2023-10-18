import pandas as pd
import matplotlib.pyplot as plt

db = pd.read_csv('VJVentas.csv')
rpg = db.where((db["Genre"] == 'Role-Playing'))  
shooter = db.where((db["Genre"] == 'Shooter'))
action = db.where((db["Genre"] == 'Action'))
sports = db.where((db["Genre"] == 'Sports'))
racing = db.where((db["Genre"] == 'Racing'))

plt.scatter(rpg["NA_Sales"],rpg["JP_Sales"], s=20, color="red")
plt.scatter(shooter["NA_Sales"],shooter["JP_Sales"], s=20, color="gray")
plt.scatter(action["NA_Sales"], action["JP_Sales"], s=20, color="blue")
plt.scatter(sports["NA_Sales"], sports["JP_Sales"], s=20, color="green")
plt.scatter(racing["NA_Sales"], racing["JP_Sales"], s=20, color="purple")

plt.xlabel("Ventas en Norte América")
plt.ylabel("Ventas en Japón")

plt.legend(bbox_to_anchor=(1,0.2))
plt.show()