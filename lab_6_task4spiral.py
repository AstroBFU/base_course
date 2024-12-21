import matplotlib.pyplot as plt
import numpy as np

def spiral(k):
    phi = np.arange(0, 8*(np.pi), 0.1)
    r = k * phi
    x = r * np.cos(phi)
    y = r * np.sin(phi)

    plt.plot(x, y, label="Архимедоа спираль")
    plt.xlabel("Coord - x")
    plt.ylabel("Coord - y")
    plt.title("Архимедоа спираль")
    plt.legend()
    plt.grid()
    plt.axis('equal')
    
    plt.savefig('fig_task4_spiral.png')

spiral(float(input("Введите значение k: ")))