import matplotlib.pyplot as plt
import numpy as np

plt.plot([1.1, 5.1], [1.5, 5.5])

plt.xlabel('Coord: x') 
plt.ylabel('Coord: y')
plt.legend()
plt.title('Base')
plt.grid()
plt.savefig('pic_1.png')


