"""
Crear directorios en una ruta
"""

from os import makedirs, walk


def crearDirs():
    path = "../directorios2/"
    L = ["excel/xlsx", "word", "py", "java"]
    for d in L:
        makedirs(path + d)


def leerDirs(path):
    directorio, subdirectorios, ficheros = next(walk(path))
    print("directorio: ", directorio)
    print("subdirectorios: ", subdirectorios)
    print("ficheros: ", ficheros)


# leerDirs("../directorios")
crearDirs()
