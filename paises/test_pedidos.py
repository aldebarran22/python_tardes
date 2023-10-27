"""
Test para comprobar el funcionamiento de la exportación de Pedidos
"""

import pandas as pd
from unittest import TestCase, main
from export_pedidos import exportarPaises, path, pathDestino
from os import listdir, remove

class TestPedidos(TestCase):
    def setUp(self):
        exportarPaises()

    def testNumFicheros(self):
        """
        Comprobar si el número de ficheros es igual
        que el número de países distintos hay en Pedidos.txt
        """
        print(listdir(pathDestino))

    def tearDown(self):
        for f in listdir(pathDestino):
            remove(pathDestino+f)


if __name__ == "__main__":
    main()  # Lanzar las pruebas
