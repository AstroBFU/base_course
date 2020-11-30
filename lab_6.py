import matplotlib.pyplot as plt
import numpy as np

def parabola(a = 1, b = 1, c = 1, title = "parabola"):
    x = np.arange(-20, 20, 0.01)
    y = a*x**2 + b*x + c

    plt.plot(x, y, color='red', label="graph")

    plt.title(title)
    plt.legend()

    plt.show()

def hyperbola(k = 1, title="hyperbola"):
    x = np.arange(-20, 20, 0.01)
    y = k/x
    y = np.ma.masked_less(y, -10)
    y = np.ma.masked_greater(y, 10)

    plt.plot(x, y, color='red', label="graph")

    plt.title(title)
    plt.legend()

    plt.show()

parabola()
hyperbola() 