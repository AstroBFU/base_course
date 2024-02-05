import matplotlib.pyplot as plt
import numpy as np

def elps(rad = 10, a = 9, b = 4):
    x = np.arange(-2*rad, 2*rad, 0.1)
    y = np.arange(-2*rad, 2*rad, 0.1)

    X, Y = np.meshgrid(x, y)

    fxy = X**2/a**2 + Y**2/b**2 - 1

    plt.contour(X, Y, fxy, levels=[0])
    plt.axis('equal')
    plt.savefig('fig_lab_6_task_3.png')
if __name__ == '__main__':
    elps()
