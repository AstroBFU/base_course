import numpy as np
g = 9.81
x_0 = 0
y_0 = 0
v_0 = 15
alpha = 45 * np.pi /180
vx_0= v_0 * np.cos(alpha)
vy_0 = v_0 * np.sin(alpha)

time= []
x_coords = []
y_coords = []

for t in np.arange(0, 5, 0.01):
    x = x_0 + vx_0 * t
    y = y_0 + vy_0 * t - g*t**2 /2

    time.append(t)
    x_coords.append(x)
    y_coords.append(y)
print(t)
print(x)
print (y)


