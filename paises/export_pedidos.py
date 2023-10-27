import pandas as pd

path = "../../practicas/Analisis Datos/merge/Pedidos.txt"
pathDestino = "../../practicas/Analisis Datos/merge/paises/"


def exportarPaises():
    df = pd.read_csv(path, sep=";")
    # print("Datos cargados: ", df.shape)
    listaPaises = list(df.pais.unique())
    listaPaises.sort()
    for pais in listaPaises:
        fichero = pathDestino + f"{pais}.csv"
        df[df.pais == pais].to_csv(fichero, sep=";", index=False, decimal=",")
        print(f"Generando fichero: {fichero}")


if __name__ == "__main__":
    exportarPaises()
