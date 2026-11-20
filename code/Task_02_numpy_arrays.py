
import numpy as np

temperatures_c = np.array([18.5,18.0,17.8,17.5,17.9,19.0,21.5,23.8,25.6,27.1,28.3,29.0,
                           29.4,29.1,28.5,27.6,26.2,24.8,23.4,22.1,21.0,20.2,19.6,19.0])
print("Mean:", temperatures_c.mean())
print("Minimum:", temperatures_c.min())
print("Maximum:", temperatures_c.max())
print("Fahrenheit:", 1.8 * temperatures_c + 32)
