

import numpy as np

A = np.array([[4.,2.],[8.,12.]])
b = np.array([20.,72.])
solution = np.linalg.solve(A,b)
print("Solution:", solution)
print("Verification:", A @ solution)
print("Residual:", b - A @ solution)
