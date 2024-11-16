import numpy as np

array = np.array([])
while len(array) <= 10:
    a = input()
    if a == "":
        break
    a = int(a)
    array = np.append(array, [a])
print(array)