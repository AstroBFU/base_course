import matplotlib.pyplot as plt 
import numpy as np 

phi = np.arange(0.01, 8*np.pi, 0.1)
r = 0.2/np.sqrt(phi)

x = np.cos(phi)*r
y = np.sin(phi)*r

plt.plot(x, y)
plt.axis('equal')
plt.savefig('fig_lab_6_task_4_3.png')