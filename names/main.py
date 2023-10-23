import pandas as pd
from os import listdir
import re


def cargaDataFrame(path):
    df = pd.read_csv(path, header=None, names=["nombre", "sexo", "total"])
    df.set_index(["nombre", "sexo"], inplace=True)
    return df


def sumarDosDF():
    df = cargaDataFrame("names/yob2015.txt")
    df2 = cargaDataFrame("names/yob2016.txt")
    suma = df.add(df2, fill_value=0)
    suma.sort_values(by="total", ascending=False, inplace=True)
    print(suma.head())


def seleccionarFicheros(path, añoini, añofin):
    # Seleccionar el rango de ficheros a partir de los parámetros:
    patron = "yob(\d{4})\.txt"
    L = []
    for f in listdir(path):
        obj = re.match(patron, f)
        if obj:
            año = int(obj.groups()[0])
            if añoini <= año <= añofin:
                df = cargaDataFrame(path + f)
                L.append(df)

    dfTodos = pd.concat(L)
    dfTodos.sort_values(by=["nombre", "total", "sexo"], ascending=False, inplace=True)
    print(dfTodos.loc['Isabella','F'])
    print('Numfilas: ', dfTodos.shape[0])


def seleccionarFicheros2(path, añoini, añofin):
    primeraVez = True

    for i in range(añoini, añofin + 1):
        try:
            fichero = path + f"yob{i}.txt"
            print(fichero)
            df = cargaDataFrame(fichero)
            if primeraVez:
                total = df
                primeraVez = False
            else:
                total = total.add(df, fill_value=0)

        except Exception as e:
            print(e)

    total.sort_values(by="total", ascending=False, inplace=True)
    print(total.head(5))


if __name__ == "__main__":
    # sumarDosDF()
    seleccionarFicheros("../../practicas/Analisis datos/names/", 2010, 2015)
