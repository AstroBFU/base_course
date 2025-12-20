import matplotlib.pyplot as plt
import numpy as np
def stupenka(N):
    x=np.arange(0,N+1,0.0005)
    y=x//1
    plt.plot(x,y)
    plt.savefig('1111.png')
    plt.close
stupenka(3)