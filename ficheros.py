"""Trabajo con ficheros en Python
En python: '' 0 False None --> False

"""

from os import listdir


def leerFichero(path):
    f = None
    try:
        f = open(path, "r")
        txt = f.read()
        return txt

    except Exception as e:
        print(e.__class__.__name__, e)
    finally:
        if f != None:
            f.close()


def escribirFichero(path, txt):
    f = None
    try:
        f = open(path, "w")
        f.write(txt)

    except Exception as e:
        print(e.__class__.__name__, e)
    finally:
        if f != None:
            f.close()


def cargaDictFromFile(path, sepFila="\n", sepCol=";"):
    try:
        registros = list()
        texto = leerFichero(path)
        L = texto.split(sepFila)
        cab = L[0].split(sepCol)

        for linea in L[1:]:
            datos = linea.split(sepCol)
            d = dict(zip(cab, datos))
            registros.append(d)
        return registros

    except Exception as e:
        print("ERROR: ", e)


def dictToXML(L, tagRoot, tag):
    xml = "<?xml version='1.0'?>"
    xml += f"<{tagRoot}>"
    for dicc in L:
        xml += f"<{tag}>"
        for k, v in dicc.items():
            xml += f"<{k}>{v}</{k}>"
        xml += f"</{tag}>"
    xml += f"</{tagRoot}>"
    return xml


if __name__ == "__main__":
    path_txt = "../practicas/Analisis Datos/merge/"
    for fichero in listdir(path_txt):
        t = fichero.partition(".")
        if t[2] == "txt":
            tagRoot = t[0].lower()
            tag = tagRoot[:-1]  # Quitar la última letra
            # f-string
            path = f"../practicas/Analisis Datos/merge/{fichero}"
            d = cargaDictFromFile(path)
            xml = dictToXML(d, tagRoot, tag)
            escribirFichero(path.replace(".txt", ".xml"), xml)
