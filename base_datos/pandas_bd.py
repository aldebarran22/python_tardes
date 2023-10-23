import sqlite3 as dbapi
from os.path import isfile

path = "empresa3.db"
if isfile(path):
    print("ok")
else:
    raise FileNotFoundError(f"No existe el fichero {path}")
