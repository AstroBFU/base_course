import numpy as np
N = 4
M = 5

A = np.zeros((M,N))
print(A)

for m in range  (M):
  for n in range (N):
    A[m, n] = np.sin(N * (n + 1) + M * (m + 1))
    if s > 0:
      A[m, n] = s

print(A)