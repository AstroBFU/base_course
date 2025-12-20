import matplotlib.pyplot as plt
import numpy as np


def parabola_plotter(a=1, b=1, c=0):

    x = np.arange(-10, 10, 0.01)
    y = a*x**2 + b*x + c

    plt.plot(x, y, label='my parabola')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.title('Parabola plotter')
    plt.legend()

    plt.savefig('fig_3.png')


if __name__ == '__main__':
    parabola_plotter()