import matplotlib.pyplot as plt
import numpy as np
def hyperbola(k=10, a=1, b=10, c=1):
    x = np.arange(a, b, c)
    y = k/x
    plt.plot(x, y)
    plt.savefig('fig_lab_6_task_2.png')

if __name__ == '__main__':
    hyperbola(k=42, a=0.1, b=10, c=0.01 )
