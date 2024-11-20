import numpy as np

def multiply_elements(arr):
    return np.prod(arr)

array = np.array([1, 2, 3, 4, 5])
print(multiply_elements(array))
