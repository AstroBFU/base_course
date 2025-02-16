import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

t1 = np.linspace(np.pi, 0, 10)
x1 = 2 * np.cos(t1)
y1 = 2 * np.sin(t1)

x2 = np.arange(2.1, 4, 0.2)
y2 = np.zeros(len(x2))

x = np.append(x1, x2)
y = np.append(y1, y2)

t3 = np.linspace(np.pi, 2*np.pi, 10)
x3 = 6 + 2 * np.cos(t3)
y3 = 2 * np.sin(t3)

x = np.append(x, x3)
y = np.append(y, y3)

spline_coords, figure_spline_part = interpolate.splprep([x, y], s=0)
spline_curve = interpolate.splev(figure_spline_part, spline_coords)

plt.plot(x, y, 'bo')
plt.plot(spline_curve[0], spline_curve[1], 'g')
plt.axis('equal')
plt.savefig('resultsinterpolate_complex_area.png')
