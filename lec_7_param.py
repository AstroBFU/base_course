import matplotlib.pyplot as plt
import numpy as np

alpha = np.arange(-2*np.pi, 2*np.pi, 0.1) # Параметр
R = 3
x = R * np.cos(alpha)
y = R * np.sin(alpha)

plt.plot(x,y,ls='--', lw=3)

plt.axis('equal')

plt.show()
