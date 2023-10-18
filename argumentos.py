"""
Capturar y procesar los argumentos que pasamos al script
"""

import sys

if len(sys.argv) == 1:
    print("Faltan parámetros: argumentos <param1> <param2>")
else:
    print('continuar ...')