import matplotlib.pyplot as plt 
import numpy as np
x = [1,1,5,5,1]
y = [1,5,5,1,1]
plt.plot(x,y, color='r', label='lunchte', marker='>',ms=5)
plt.axis('equal')
plt.show()
