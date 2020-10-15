import numpy as np
A=np.array([[1,2,3],[4,5,6]])

print(A[1,:])
print(A[:,1])

B=A[:,::-1]
print(B)

#[::]=[0:len:1]
#[start:stop:step]