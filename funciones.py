"""Paso de parámetros a funciones"""


def funcion(ob1, ob2, op1=1, op2=2, *args, **kwargs):
    """Pruebas con parametros"""
    print("obligatorios: ", ob1, ob2)
    print("opcionales: ", op1, op2)
    print("args: ", args)
    print("kwargs: ", kwargs)
    print()


if __name__ == "__main__":
    # El módulo se está ejecutando
    funcion(10, 20)
    funcion(1, 2, 3, 4, 5, 6, 7, 8)
    funcion(1, 2, x=10, y=20)
    funcion(1, 2, x=10, y=20)
