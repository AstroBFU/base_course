import numpy as np

x0 = 5
y0 = 6
v0 = 7
g = 10
t = np.arange(0, 5, 0.1)
x = x0 + v0 * t
y = y0 + v0 * t - g * t**2 / 2
print(y)

coords = np.zeros((len(t), 3))
for i in range(len(t)):
  coords[i, 0] = t[i]
  coords[i, 1] = x[i]
  coords[i, 2] = y[i]

print(coords)