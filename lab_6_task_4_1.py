import matplotlib.pyplot as plt 
import numpy as np 
phi = np.arange(0, np.pi*8, 0.1)
r = np.e**(0.1*phi)

x = np.cos(phi)*r
y = np.sin(phi)*r

plt.plot(x, y)
plt.savefig('fig_lab_6_task_4_1.png')




