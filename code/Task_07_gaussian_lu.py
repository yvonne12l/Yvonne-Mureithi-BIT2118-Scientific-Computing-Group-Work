

import numpy as np
from scipy.linalg import lu_factor, lu_solve

A = np.array([[4.,-1.,0.],[-1.,4.,-1.],[0.,-1.,3.]])
b = np.array([15.,10.,10.])
lu, piv = lu_factor(A)
x = lu_solve((lu,piv), b)
print("Solution:", x)
print("Verification:", A @ x)
