"""
Creación y uso de diccionarios en python
"""

d1 = {'a': 1, 'b':2, 'c':3, 'd':4, 'e':5}
print('z' in d1)
print(3 in d1.values())

s = "adios"
L = list(range(5))
d2 = dict(zip(s, L))
print(d2)

# invertir dict:
d3 = dict(zip(d2.values(), d2.keys()))
print(d3)