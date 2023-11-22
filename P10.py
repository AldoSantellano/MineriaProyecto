from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

def open_file(path: str) -> str:
    content = ""
    with open(path, "r") as f:
        content = f.readlines()
    return " ".join(content)

db = pd.read_csv("VJVentas.csv", usecols=[1])
#Para que pueda funcionar con normalidad este código se tiene que cambiar la ruta en donde se encuentra el archivo titulos.txt.
np.savetxt(r'D:\GitHub\MineriaProyecto\titulos.txt', db.values, fmt='%s')


all_words = ""
frase = open_file("titulos.txt") 
palabras = frase.rstrip().split(" ")

Counter(" ".join(palabras).split()).most_common(10)
for arg in palabras:
    tokens = arg.split()
    all_words += " ".join(tokens) + " "

print(all_words)
wordcloud = WordCloud(
    background_color="white", min_font_size=5
).generate(all_words)

plt.close()
plt.figure(figsize=(5, 5), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.savefig("WordCloud.png")
plt.close()