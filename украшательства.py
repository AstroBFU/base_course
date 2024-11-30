import matplotlib.pyplot as plt

# допы для графика

x = [1,2,3]
y = [4,5,6]

plt.plot(x,y,color='g', label = 'graf 1', ms = 5)
plt.plot(y,x,color='r', label = 'graf 2', ms = 3)

plt.xlabel('coord: x') 
plt.ylabel('coord: y') 
plt.legend()
