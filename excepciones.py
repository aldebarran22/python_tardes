"""
Excepciones que se pueden producir con list y dict
"""

def sumar(a,b):
    return a+b

try:
    L = list(range(10))
    print(L)
    print("suma: ", sum(L))
    print(L[30])
except IndexError as e:
    print(e.__class__.__name__, e)

try:
    d = {"1": 1, "2": 2, "3": 3, "4": 4}
    print(d)
    # print(d['0'])
    print(d.get("0", "no existe la clave"))
    print(d.pop("0", "No puedo borrar el 0"))
    del d["4"]
    print(d)

except KeyError as e:
    print(e.__class__.__name__, e)


try:
    i = sumar
    print(i(12,55))
    j = 100
    j() # Intentar ejecutar algo que NO es una función
except Exception as e:
    print(e.__class__.__name__, e)


try:
    n = 100
    print(n[0]) # Intentar indexar algo que NO es indexable!
except Exception as e:
    print(e.__class__.__name__, e)
