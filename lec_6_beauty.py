import mathlotlib.pyplot as plt
import numpy as np
x = [3, 4, 5]
y = [40, 10, 30]

plt.plot(x, y, color='g', label='luchte', marker='^', ms=5)
plt.xlabel('coord: x')
plt.ylabel('coord: y')
plt.legende()
plt.title('Base')
plt.grid()
plt.show()
