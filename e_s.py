"""
Pruebas con el puntero de L/E en un fichero
"""
path = "yob1880.txt"


f = open(path, "rb")
for linea in f:
    linea = linea.rstrip()  # Limpia el salto de linea del final
    print(linea, f.tell())
f.close()


"""
f = open(path, "r")
lineaBuscar = "Minnie,F,1746"
existe = False
while True:
    linea = f.readline()
    # print(linea, end=' ')

    if not linea:
        break
    linea = linea.rstrip()
    if linea == lineaBuscar:
        existe = True
        print(linea)
        break
if existe:
    print(lineaBuscar, "encontrada")
f.close()
"""
