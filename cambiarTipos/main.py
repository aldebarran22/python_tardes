import pandas as pd


def cambiarTipo(path):
    df = pd.read_csv(path, sep=";")
    # Limpiar espacios en blanco de los nombres de las columnas
    df.columns = [col.strip() for col in df.columns]
    df["Lat"] = pd.to_numeric(df["Lat"].str[:-1], downcast="float")
    df["Lon"] = pd.to_numeric(df["Lon"].str[:-1], downcast="float")
    df["Wind"] = pd.to_numeric(df.Wind.str.replace(" mph ",""), downcast="integer")
    df["Pressure"] = pd.to_numeric(df.Pressure.str.replace(" mb ",""), downcast="integer")
    print(df.info())


if __name__ == "__main__":
    cambiarTipo("IRMA.csv")
