import numpy as np

kernel = np.array([1, 1, 1, 2]).reshape((2, 2))
print(kernel)
print(np.linalg.inv(kernel))
