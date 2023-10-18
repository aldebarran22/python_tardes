import sys

sys.path.append("D:/temp")
for i in sys.path:
    print(i)

from funcion_abc import operar

print("operar: ", operar(10, 20))
