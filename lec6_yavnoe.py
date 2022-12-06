import matplotlib.pyplot as plt
import numpy as np

def parabola_plotter(a=1, b=1, c=0, title='Parabola plotter'):
    x = np.arange(-10, 10, 4)
    y = a*x**2 + b*x + c

    plt.plot(x, y, label='my parabola')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.title(title)
    plt.legend()
    plt.savefig('pig_png')
parabola_plotter()
