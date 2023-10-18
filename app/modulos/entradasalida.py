"""
Módulo para leer y escribir ficheros
"""

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
