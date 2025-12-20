import matplotlib.pyplot as plt
import numpy as np
def fig_lissag(a=1, A=1, B=3,b=2):
    t = np.linspace(0, 2 * np.pi, 500)
    g=np.pi/2
    x=A*np.sin(a*t+b)
    y=B*np.sin(b*t)
    plt.plot(x,y)
    plt.savefig('fig_lissag_1.jpg') 
    plt.close
fig_lissag()