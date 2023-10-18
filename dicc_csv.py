"""Convertir un bloque de texto en CSV a una lista de dict"""

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

empleados = list()
L = texto.split("\n")
cab = L[0].split(';')+['tno']

for linea in L[1:]:
    datos = linea.split(';')
    d = dict(zip(cab, datos))
    empleados.append(d)

# El nombre del tercer empleado:
print(empleados[2]['nombre'])
