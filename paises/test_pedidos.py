"""
Test para comprobar el funcionamiento de la exportación de Pedidos
"""

import pandas as pd
from unittest import TestCase, main
from export_pedidos import exportarPaises, path, pathDestino
from os import listdir, remove


class TestPedidos(TestCase):
    def __init__(self, param):
        TestCase.__init__(self, param)
        self.df = pd.read_csv(path, sep=";")
        self.paisesPedidos = sorted(self.df.pais.unique())

    def setUp(self):
        exportarPaises()

    def testNumFicheros(self):
        """
        Comprobar si el número de ficheros es igual
        que el número de países distintos hay en Pedidos.txt
        """
        # Obtener los paises del fichero de pedidos:
        mensaje = "El número de ficheros no coincide con el número de países de pedidos"
        ficheros = listdir(pathDestino)
        self.assertEqual(len(ficheros), len(self.paisesPedidos), msg=mensaje)

    def testNumRegistros(self):
        """Comprobar si el total de pedidos coincide en los ficheros y en Pedidos"""
        numFilas, _ = self.df.shape
        total = 0
        for f in listdir(pathDestino):
            dfAux = pd.read_csv(pathDestino + f, sep=";")
            total += dfAux.shape[0]

        if numFilas != total:
            self.fail(msg="No coincide la suma total de las filas de los ficheros")

    def testNombreFicheros(self):
        """Comprobar si el nombre de los ficheros coincide con los nombres de los países"""
        list_paises_dir = list([x.split(".")[0] for x in listdir(pathDestino)])
        list_paises_dir.sort()
        self.assertEqual(
            self.paisesPedidos, list_paises_dir, "Los paises son distintos"
        )

    def tearDown(self):
        for f in listdir(pathDestino):
            remove(pathDestino + f)


if __name__ == "__main__":
    main()  # Lanzar las pruebas
