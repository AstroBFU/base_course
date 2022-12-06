import matplotlib.pyplot as plt
import numpy as np

x = [3, 4, 5]
y = [40, 10, 30]

plt.plot(x, y, color='red', label='luchte', marker='>', ms=5) # color-цвет графика label- подпись графика marker- маркер графика ms - размер графика

plt.xlabel('Coord: x') 
plt.ylabel('Coord: y')
plt.legend()
plt.title('Base')
plt.grid()
plt.savefig('pic_1.png')
