import matplotlib.pyplot as plt
import numpy as np

def circle (R=1,title='circle'):
    x=np.arange(-10,10,0.1)
    y=np.arange(-10,10,0.1)
    X,Y=np.meshgrid(x,y)
    
    f_xy=X**2+Y**2
    
    plt.contour(X,Y,f_xy,levels=[R**2])
    
    plt.axis('equal')
    plt.show()
    
def ellips (a=1,b=1,title='ellips'):
    x=np.arange(-10,10,0.1)
    y=np.arange(-10,10,0.1)
    X,Y=np.meshgrid(x,y)
    
    f_xy=(X/a)**2+(Y/b)**2
    
    plt.contour(X,Y,f_xy,levels=[1])
    
    plt.axis('equal')
    
    plt.show()
circle(8)
ellips(8,2)    