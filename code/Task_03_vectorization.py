
import numpy as np
import timeit

latency = np.linspace(5, 250, 1_000_000)
vectorized = latency ** 2
loop_time = timeit.timeit(lambda: [x ** 2 for x in latency], number=1)
vectorized_time = timeit.timeit(lambda: latency ** 2, number=1)
print("First five squared values:", vectorized[:5])
print("Loop time:", loop_time)
print("Vectorized time:", vectorized_time)
