import matplotlib.pyplot as plt
import numpy as np
def logarifm_spir(b):
    phi=np.arange(0,8*np.pi,0.01)
    r=np.exp(b*phi)

    x=r*np.cos(phi)
    y=r*np.sin(phi)

    plt.plot(x,y)
    plt.savefig('fig_121.jpg') 
logarifm_spir(0.11)


