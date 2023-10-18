"""
Test para probar paquetes y subpaquetes en Python
"""

from os import listdir, getcwd

import modulos.formatos as fmt
import modulos.entradasalida as es

#from modulos.entradasalida import escribirFichero
#from modulos.formatos import cargaDictFromFile, dictToXML

if __name__ == "__main__":    
    path_txt = "../practicas/Analisis Datos/merge/"
    for fichero in listdir(path_txt):
        t = fichero.partition(".")
        if t[2] == "txt":
            tagRoot = t[0].lower()
            tag = tagRoot[:-1]  # Quitar la última letra
            # f-string
            path = f"../practicas/Analisis Datos/merge/{fichero}"
            d = fmt.cargaDictFromFile(path)
            xml = fmt.dictToXML(d, tagRoot, tag)
            es.escribirFichero(path.replace(".txt", ".xml"), xml)
