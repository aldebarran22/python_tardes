"""
Funciones para cargar un diccionario de un CSV
Y pasar de un diccionario a XML
"""
try:
    from modulos.entradasalida import leerFichero
except:
    from entradasalida import leerFichero

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

if __name__=='__main__':
    print(cargaDictFromFile('../practicas/Analisis Datos/merge/Empresas.txt'))