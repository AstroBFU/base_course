import matplotlib.pyplot as plt
import numpy as np

x = [3,4,5]
y = [40,10,30]
plt.plot(x,y, color='g', label='lunchte', marker='>',ms=5)
#----Украшательства----
plt.xlabel('Coord: x')
plt.ylabel('Coord: y')
plt.legend()
plt.title('Base')
plt.grid()
plt.show()
