import pandas as pd
import numpy as np

print("pandas: ", pd.__version__)
print("numpy: ", np.__version__)

if np.__version__ != "1.24.4":
    print("Versión necesaria de numpy: 1.24.4")
    exit()
else:
    print("Todo ok!")
