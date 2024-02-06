import matplotlib.pyplot as plt 
import numpy as np 

phi = np.arange(0.01, 8*np.pi, 0.1)
r = np.sin(5*phi)

x = np.cos(phi)*r
y = np.sin(phi)*r

plt.plot(x, y)
plt.savefig('fig_lab_6_task_4_4.png')