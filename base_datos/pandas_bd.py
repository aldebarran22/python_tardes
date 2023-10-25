import sqlite3 as dbapi
from os.path import isfile
import pandas as pd
from xml.etree.ElementTree import Element, SubElement, Comment, tostring, ElementTree


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
        # sql = """select pais, sum(importe) as total
        # from pedidos group by pais order by 2 desc"""
        sql = "select * from pedidos"
        df = pd.read_sql(sql, con)

        # Agrupar por un campo
        grupo = df.importe.groupby(df.pais)
        print(grupo.max())

        # Agrupar por dos campos:
        grupo2 = df["importe"].groupby([df["pais"], df["idcliente"]])
        print(grupo2.sum())

        con.close()


def exportarBDXML():
    path = "empresa3.db"
    if isfile(path):
        con = dbapi.connect(path)
        sql = """select pais, sum(importe) as total
        from pedidos group by pais order by 2 desc"""
        df = pd.read_sql(sql.replace("\n", " "), con)
        top = Element("paises")
        comentario = Comment(sql)
        top.append(comentario)
        for num, serie in df.iterrows():
            pais = Element("pais")
            nombre = SubElement(pais, "nombre")
            nombre.text = serie["pais"]
            total = SubElement(pais, "total")
            total.text = "%.2f" % serie["total"]
            top.append(pais)

        # Grabar a un fichero:
        tree = ElementTree()
        tree._setroot(top)
        tree.write("paises.xml")


if __name__ == "__main__":
    exportarBDXML()
