import sqlite3 as dbapi
from os.path import isfile
import pandas as pd


def listarPedidos():
    path = "empresa3.db"
    if isfile(path):
        con = dbapi.connect(path)
        cur = con.cursor()
        sql = "select * from pedidos"
        cur.execute(sql)
        for t in cur.fetchall():
            print(t)
        cur.close()
        con.close()
    else:
        raise FileNotFoundError(f"No existe el fichero {path}")


def cargarPedidos():
    path = "empresa3.db"
    if isfile(path):
        con = dbapi.connect(path)
        sql = "select * from pedidos"
        df = pd.read_sql(sql, con)
        print(df.head())
        con.close()

cargarPedidos()
