import matplotlib.pyplot as plt
import numpy as np


def giperbola_plotter(x_min, x_max, N):

    x = np.linspace(x_min, x_max, N)
    y = 1/(x+0.1)

    plt.plot(x, y, label='my giperbola')
    plt.savefig('gip_33.png')
    plt.close()
giperbola_plotter(-50, 50,10)