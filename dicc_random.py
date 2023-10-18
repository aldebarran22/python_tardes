"""

"""

import string
from random import randint

d = dict()
for i in range(10):
    k = randint(1,20)
    palabra =""
    for j in range(5):
        n = randint(0, len(string.ascii_uppercase)-1)
        letra = string.ascii_uppercase[n]
        palabra+=letra
        
    d[k] = palabra
print(d)

    