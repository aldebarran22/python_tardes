"""
Calcular un histograma del 1 al 20  con 1000 números al azar.
"""

from random import randint
from collections import Counter

L = [randint(1,20) for _ in range(1000)]
print(L[:10])

L.sort()
d = dict.fromkeys(range(1,21), 0)
print(d)

c = Counter(L)
d = dict(c)
L = sorted(d.items(), key=lambda t: t[0])
print(L)

# El que mas se repite:
L2 = sorted(d.items(), key=lambda t: t[1], reverse=True)
print(L2[0])
