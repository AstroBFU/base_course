	
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Определяем переменную величину и количество кадров
frames = 200
tau = np.linspace(0, 5, frames)

def matrix(z, cols):
	rows = int(len(z) / cols)
	d = np.array(z).reshape((rows, cols))
	d = list(map(list, d))
	return d
  
def betweensGen(get, mainPIdx):
    mainP = get[mainPIdx]
    Fx = []
    Fy = []
    for currentP in get:
        if currentP != mainP:
            r = abs(np.sqrt((mainP[0] - currentP[0])**2 + (mainP[2] - currentP[2])**2))
            Fx.append((k * mainP[4] * currentP[4] * (mainP[0] - currentP[0])) / r ** (3/2))
            Fy.append((k * mainP[4] * currentP[4] * (mainP[2] - currentP[2])) / r ** (3/2))
            Fx.append((-G * mainP[5] * currentP[5] * (mainP[0] - currentP[0])) / r ** (3/2))
            Fy.append((-G * mainP[5] * currentP[5] * (mainP[2] - currentP[2])) / r ** (3/2))

    return Fx, Fy		
	
def collision(get, mainPIdx):
    mainP = get[mainPIdx]
    vx = 0
    vy = 0
    for currentP in get:
        if currentP != mainP:
            r = abs(np.sqrt((mainP[0] - currentP[0])**2 + (mainP[2] - currentP[2])**2))
            if r <= (mainP[6] + currentP[6]):
                vx = mainP[1] * (mainP[5] - currentP[5]) / (mainP[5] + currentP[5]) + (2) * currentP[5] * currentP[1] / (mainP[5] + currentP[5])
                vy = mainP[3] * (mainP[5] - currentP[5]) / (mainP[5] + currentP[5]) + (2) * currentP[5] * currentP[3] / (mainP[5] + currentP[5])
            else:
                vx = mainP[1]
                vy = mainP[3]
    return vx, vy
    


# Определяем функцию для системы диф. уравнений
def move_func(z, t):
    get = matrix(z, 7)
    ret = []
			
    for i in range(len(get)):
        Fx, Fy = betweensGen(get, i)
        
        q = get[i][4]
        m = get[i][5]
        r = get[i][6]
        
        ret.append(get[i][1])
        ret.append(sum(Fx) / m)
        ret.append(get[i][3])
        ret.append(sum(Fy) / m)
        ret.append(q)
        ret.append(m)
        ret.append(r)
    	
    return tuple(ret)

# Определяем начальные значения и параметры
numberOfParticles = 3

AE = 149 * 10**9
k = 9 * 10**9
G = 6.67 * 10**-11

z0 = [0, 0, 0, 0, 5 * 10**-5, 5, 0.5,
      5, -5, 0, 2, -10**-4, 1, 0.5,
      -1, -2, -1, -1, -10**-4, 1, 0.5]

'''
x координата
vx скорость
y координата
vy скорость
q заряд
m масса
r радиус
'''

# Решаем систему диф. уравнений

def solve(mainPNum):
    x = []
    y = []
    for k in range(frames - 1):

        t = [tau[k], tau[k + 1]]

        sol = odeint(move_func, z0, t)

        z0[mainPNum * 7 - 7] = sol[1, mainPNum * 7 - 7]
        z0[mainPNum * 7 - 5] = sol[1, mainPNum * 7 - 5]

        x.append(z0[mainPNum * 7 - 7])
        y.append(z0[mainPNum * 7 - 5])

        z0[mainPNum * 7 - 6] = sol[1, mainPNum * 7 - 6]
        z0[mainPNum * 7 - 4] = sol[1, mainPNum * 7 - 4]

        res = collision(matrix(z0, 7), mainPNum - 1)

        z0[mainPNum * 7 - 6] = res[0]
        z0[mainPNum * 7 - 4] = res[1]
    return (x, y)

'''
sol = odeint(move_func, z0, t)
def solve_func(i, key, mainPNum):
    if key == 'point':
        x = sol[i, mainPNum * 7 - 7]
        y = sol[i, mainPNum * 7 - 5]
    else:
        x = sol[:i, mainPNum * 7 - 7]
        y = sol[:i, mainPNum * 7 - 5]
    return x, y
'''
# Строим решение в виде графика и анимируем
fig, ax = plt.subplots()


part1, = plt.plot([], [], 'o', color='r')
trace1, = plt.plot([], [], '-', color='r')

part2, = plt.plot([], [], 'o', color='b')
trace2, = plt.plot([], [], '-', color='b')

part3, = plt.plot([], [], 'o', color='b')
trace3, = plt.plot([], [], '-', color='b')
'''
part4, = plt.plot([], [], 'o', color='r')
trace4, = plt.plot([], [], '-', color='r')
'''
def animate(i):
    print(round(i / (frames / 100), 1), '%')
    part1.set_data((solve(1)[0], solve(1)[1]))
    #trace1.set_data(solve_func(i, 'line', 1))

    part2.set_data((solve(2)[0], solve(2)[1]))
    #trace2.set_data(solve_func(i, 'line', 2))

    part3.set_data((solve(3)[0], solve(3)[1]))
    #trace3.set_data(solve_func(i, 'line', 3))
'''   
    part4.set_data(solve_func(i, 'point', 4))
    trace4.set_data(solve_func(i, 'line', 4))
'''

ani = FuncAnimation(fig,
                    animate,
                    frames=frames,
                    interval=30)

edge = 20
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani.save('qlon.gif')