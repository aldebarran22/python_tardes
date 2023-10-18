"""
Relleno de ceros o espacios en la consola
"""
L = [(2, 45, 55), (8, 2, 12), (5, 7, 23), (5, 6, 7)]
# 02:45:55, 08:02:12 ...
fichero = open("horas.txt", "w")
for t in L:
    print("%02d:%02d:%02d" % t, file=fichero)
fichero.close()
