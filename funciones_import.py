import funciones

modulo = globals()["funciones"]
f = getattr(modulo, "funcion")
f2 = modulo.funcion
print(dir(modulo))
print(type(f))
print(type(modulo))
print(f(10, 10))
print("f2:", type(f2))
