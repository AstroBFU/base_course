import matplotlib.pyplot as plt
import numpy as np
def rosa_spir(k):
    phi=np.arange(0,8*np.pi,0.01)
    r=np.sin(k*phi)

    x=r*np.cos(phi)
    y=r*np.sin(phi)

    plt.plot(x,y)
    plt.savefig('rosa_1.jpg') 
rosa_spir(10)