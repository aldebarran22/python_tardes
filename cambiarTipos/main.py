import pandas as pd
import numpy as np


def cambiarTipo(path):
    df = pd.read_csv(path, sep=";")
    # Limpiar espacios en blanco de los nombres de las columnas
    df.columns = [col.strip() for col in df.columns]
    df["aux"] = df.Date + " 2005 " + df.Time.str.replace(" GMT", "")
    df["Lat"] = pd.to_numeric(df["Lat"].str[:-1], downcast="signed")
    df["Lon"] = pd.to_numeric(df["Lon"].str[:-1], downcast="signed")
    df["Wind"] = pd.to_numeric(df.Wind.str.replace(" mph ", ""), downcast="integer")
    df["Pressure"] = pd.to_numeric(
        df.Pressure.str.replace(" mb ", ""), downcast="integer"
    )
    df["Date_Time"] = pd.to_datetime(df.aux, format="%b %d %Y %H:%M")
    df = df[["Date_Time", "Lat", "Lon", "Wind", "Pressure"]]
    print(df.head(5))


if __name__ == "__main__":
    cambiarTipo("IRMA.csv")
