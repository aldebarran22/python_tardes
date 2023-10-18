"""
A partir de dos bloques de texto obtener las
líneas iguales y las que son distintas
"""
texto="""id;nombre;cargo
1;Davolio;Representante de ventas
2;Fuller;Vicepresidente comercial
3;Leverling;Representante de ventas
4;Peacock;Representante de ventas
5;Buchanan;Gerente de ventas
6;Suyama;Representante de ventas
7;King;Representante de ventas
8;Callahan;Coordinador ventas interno
9;Dodsworth;Representante de ventas"""

texto2="""id;nombre;cargo
0;Juan;Representante de ventas
1;Davolio;Representante de ventas
2;Fuller;Vicepresidente comercial
3;Leverling;Representante de ventas
4;Peacock;Representante de ventas
5;Buchanan;Gerente de ventas
6;Suyama;Gerente
7;King;Representante de ventas
8;Callahan;Coordinador ventas interno
9;Dodsworth;Gerente"""

fich1 = set(texto.split("\n")[1:])
fich2 = set(texto2.split("\n")[1:])

# Lineas comunes:
comunes = fich1 & fich2
for e in sorted(comunes):
    print(e)

# REgistros de texto2 que no estan en texto:
print('\nsoloEnTexto2:')
soloEnTexto2 = fich2 - fich1
for e in sorted(soloEnTexto2):
    print(e)

# Todos los registros sin repetidos:
print('\nTodos los registros:')
todos = fich1 | fich2
for e in sorted(todos):
    print(e)

# Todos los empleados quitando los que coincidan
# en ambos conjuntos:
print('Sin coincidentes:')
sinCoincidentes = fich1 ^ fich2
for e in sorted(sinCoincidentes):
    print(e)

