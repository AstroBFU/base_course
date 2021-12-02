import numpy
import math

N = 4
M = 5
a = numpy.zeros((N, M))

for (i, j), value in numpy.ndenumerate(a):
  res = math.sin(N * (i + 1) + M * (j + 1))
  if res < 0:
    res = 0
  a[i, j] = res

print(a)