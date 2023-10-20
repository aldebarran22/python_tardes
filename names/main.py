import pandas as pd

df = pd.read_csv("names/yob2015.txt", header=None, names=["nombre", "sexo", "total"])
df.set_index(["nombre", "sexo"], inplace=True)
print(df.head(10))

df2 = pd.read_csv("names/yob2016.txt", header=None, names=["nombre", "sexo", "total"])
df2.set_index(["nombre", "sexo"], inplace=True)
suma = df.add(df2, fill_value=0)
suma.sort_values(by="total", ascending=False, inplace=True)
print(suma.head(10))
