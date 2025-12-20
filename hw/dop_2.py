import matplotlib.pyplot as plt
import numpy as np
def fig_el(p,e):
    phi=np.arange(0,8*np.pi,0.01)
    r=p/(1+e*np.cos(phi))
    x=r*np.cos(phi)
    y=r*np.sin(phi)
    plt.plot(x,y)
    plt.savefig('fig_el_1.jpg') 
    plt.close
fig_el(57,0.6)