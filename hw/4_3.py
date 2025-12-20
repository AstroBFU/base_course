import matplotlib.pyplot as plt
import numpy as np
def gesl_spir(k):
    phi=np.arange(0.01, 8*np.pi,0.01)
    r=k/np.sqrt(phi)

    x=r*np.cos(phi)
    y=r*np.sin(phi)

    plt.plot(x,y)
    plt.axis('equal')
    plt.savefig('gesl_1.jpg') 

gesl_spir(1)
