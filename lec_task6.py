import numpy as np
a = np.array([[2, 3, 1, 4, 5, 6, 7],
     [8, 1, 3, 2, 2, 6, 8],
     [1, 4, 3, 1, 0, 2, 5],
     [4, 5, 0, 1, 3, 2, 1],
     [8, 7, 9, 1, 0, 2, 3] ])
slice = a[0:3:1,0:2:1 ]
print(slice)
slice = a[1:3, 3:5:1]
print(slice)
