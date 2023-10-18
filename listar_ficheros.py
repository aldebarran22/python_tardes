"""
Listar los ficheros de una carpeta de Windows
"""
#import os
from os import listdir

for f in listdir():
    print(f)
    print(f.partition('.'))