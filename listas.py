"""
Creación de listas, recorridos, métodos ...
"""
L = [3, 5, 6, 2, 1]

L2 = list("hola que tal")
print(L2)

L2[0] = 1000
print(L2)

L.sort()
print(L)

print(L.sort())

cadena = "hola"
cadena.upper()
print(cadena)

L1 = [3, 4, 5, 6, 2]
L2 = list(L1)
L3 = L1.copy()
L1[0] = 1000
print("L1", L1)
print("L2", L2)

from copy import deepcopy

L1 = [[3, 4], [5, 6, 2]]
# L3 = L1.copy() Copia superficial
L3 = deepcopy(L1)
L1[0] = 1000
L1[-1].append(1000)
print("L1", L1)
print("L3", L3)

L1 = [4, 2, 3, 4, 5, 6]
print(4 in L1)
print(24 in L1)

print([1, 2, 3] * 5)

# slicing: L[ini:fin-1:salto]
L = list(range(10))  # lista del 0 al 9
print(L)
print("El primero: ", L[0], L[-10])
print("El último: ", L[-1], L[9])
print("Los tres primeros: ", L[0:3], L[:3])
print("los 3 últimos: ", L[-3:])
print('Invertir', L[::-1])

L.reverse()
print(L)

print('suma: ', sum(L))
print('media: ', sum(L)/len(L))

print(list(enumerate(L)))

for pos, i in enumerate(L):
    print(pos, i)

# List comprehession:
L = [(i, 2**i) for i in range(10)]
print(L)

# range(ini, fin-1, salto)

# [(1,1,1)... (2,1,2), (2,10,20), (10, 10, 100)]
L2 = [(i, j, i*j) for i in range(1,11) for j in range(1,11)]
print(L2[:10])

from random import randint

# Números aleatorios multiplos de 3
L3 = [randint(0,100) for _ in range(20)]
print(L3)
L4 = [i for i in L3 if i % 3 == 0]
print(L4)

