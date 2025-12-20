import matplotlib.pyplot as plt
import numpy as np

def ar_spir(k):
    phi=np.arange(0,8*np.pi,0.01)
    r=k*phi

    x=r*np.cos(phi)
    y=r*np.sin(phi)

    plt.plot(x,y)
    plt.savefig('ar_1.jpg') 
ar_spir(0.11)