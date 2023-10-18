"""
Comparar operaciones entre listas y arrays de numpy
"""

import numpy as np
from datetime import datetime

N = 1000000
my_arr = np.arange(N)
my_list = list(range(N))

t1 = datetime.now()
for _ in range(30):
    my_arr2 = my_arr * 2
t2 = datetime.now()
print(f"Operaciones con numpy: {t2-t1}")

t1 = datetime.now()
for _ in range(30):
    my_list2 = [x * 2 for x in my_list]
t2 = datetime.now()
print(f"Operaciones con list: {t2-t1}")
