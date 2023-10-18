"""
Tuplas: creación, acceso, expansión de tuplas
sql = "select * from clientes where pais=?
"""

t = (1,2,3,4,)
t2 = 1,2,3
t3=(9)
print(t3, type(t3))
t4=(9,)
print(t4, type(t4))

# intercambiar variables:
a = 40
b = 34
a,b = b,a

def sumar(a,b):
    return a+b

t =(1,2)
print(sumar(*t))

d = {"a":1, "b":4}
print(sumar(**d))

L = [(8,9), (7,8), (12,1), (4,6)]
L2 = [sumar(*t) for t in L]
print(L2)

t = tuple([i**2 for i in range(10)])
print(t)

