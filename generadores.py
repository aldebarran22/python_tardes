"""Generadores en Python"""
# yield --> indica a Python que se trata de una función generadora!

def listaMul3(ini, fin, salto=1):
    """Crear una lista con múltiplos de 3"""
    L = []
    print('lista:')
    for i in range(ini, fin, salto):
        if i % 3 == 0:
            print('mul 3: ', i)
            L.append(i)
    return L

def genMul3(ini, fin, salto=1):
    print('\nGenerador:')
    for i in range(ini, fin, salto):
        if i % 3 == 0:
            print('gen 3: ', i)
            yield i
            print('yield')

for i in listaMul3(1,30):
    print(i, end=' ')
print()

for i in genMul3(1,30):
    print('bucle:', i)
print()