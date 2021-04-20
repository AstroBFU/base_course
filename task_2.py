import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frame = 20
seconds_in_year = 365 * 24 * 60 * 60
years = 1
t = np.arange(0, 300, 0.5)

G = 6.67 * 10 ** (-11)
k = 8.98755 * 10 ** 9
N: int = 0

"""
                                        Обястнение list[n * a + b]
n - номер элемента листа из которого мы хотим получить данные
a - переод list 
Переод - это количесво вставляемых подрят данных одного объекта моделирования в определённый лист
b - какие данные элемента мы хотим получить
"""


def get_dv_xdt(variable_balls: tuple, num: int):
    """
    :param variable_balls - все объекты моделирования
    :param num - номер объекта на который дейсвуют другие тела
    :return out: взаимодействие variable_balls элементов на num-ый элемент по x
    """

    out = 0.0

    for i in range(N):
        if i != num:
            # Вычисляем гравитационное взаимодействие variable_balls элементов на num-ый элемент
            out += (-G * not_variable_balls[i * 2 + 0] *
                    (variable_balls[num * 4 + 0] - variable_balls[i * 4 + 0]) /
                    ((variable_balls[num * 4 + 0] - variable_balls[i * 4 + 0]) ** 2 + (
                            variable_balls[num * 4 + 2] - variable_balls[i * 4 + 2]) ** 2) ** 1.5)

            # Вычисляем взаимодействие заряженных тел variable_balls элементов на num-ый элемент
            out += (k *
                    not_variable_balls[num * 2 + 1] * not_variable_balls[i * 2 + 1] /
                    not_variable_balls[num * 2 + 0] *
                    (variable_balls[num * 4 + 0] - variable_balls[i * 4 + 0]) /
                    ((variable_balls[num * 4 + 0] - variable_balls[i * 4 + 0]) ** 2 + (
                            variable_balls[num * 4 + 2] - variable_balls[i * 4 + 2]) ** 2) ** 1.5)
    return out


def get_dv_ydt(variable_balls: tuple, num: int):
    """
    :param variable_balls: все объекты моделирования
    :param num: номер объекта на который дейсвуют другие тела
    :return out: взаимодействие variable_balls элементов на num-ый элемент по y
    """

    out = 0.0

    for i in range(N):
        if i != num:
            # Вычисляем гравитационное взаимодействие variable_balls элементов на num-ый элемент
            out += (-G * not_variable_balls[i * 2 + 0] *
                    (variable_balls[num * 4 + 2] - variable_balls[i * 4 + 2]) /
                    ((variable_balls[num * 4 + 0] - variable_balls[i * 4 + 0]) ** 2 + (
                            variable_balls[num * 4 + 2] - variable_balls[i * 4 + 2]) ** 2) ** 1.5)

            # Вычисляем взаимодействие заряженных тел variable_balls элементов на num-ый элемент
            out += (k *
                    not_variable_balls[num * 2 + 1] * not_variable_balls[i * 2 + 1] /
                    not_variable_balls[num * 2 + 0] *
                    (variable_balls[num * 4 + 2] - variable_balls[i * 4 + 2]) /
                    ((variable_balls[num * 4 + 0] - variable_balls[i * 4 + 0]) ** 2 + (
                            variable_balls[num * 4 + 2] - variable_balls[i * 4 + 2]) ** 2) ** 1.5)
    return out


def move_func(variable, t):
    """
    :param variable: все изменияемые данные объектов моделирования
    :param t: linspace переода времяни
    :return: outs: решение диференциального уравнения
    """

    # Лист возвращяемых данных
    # Переод = 4
    # Элементы объекта: 0 = dxdt, 1 = dv_xdt, 2 = dydt, 3 = dv_ydt
    outs = []

    # Для каждего моделируемого объекта вычислем возвращяемые даннные
    for j in range(N):
        # Вычисляем dxdt
        outs.append(variable[j * 4 + 1])
        # Вычисляем dv_xdt
        outs.append(get_dv_xdt(variable, j))
        # Вычисляем dydt
        outs.append(variable[j * 4 + 3])
        # Вычисляем dv_ydt
        outs.append(get_dv_ydt(variable, j))

    return outs


# Лист не изменяемых данных моделируемых объектов
# Период = 2
# Данные одного моделируемого объекта: 0 = масса, 1 = зарят
not_variable_balls = []

# Лист изменяемых данных моделируемых объектов
# Период = 4
# Данные одного моделируемого объекта: 0 = x, 1 = вектор x, 2 = y, 3 = вектор y
variable = []


def ball(mas: float, electric_charge: float, x: float, v_x: float, y: float, v_y: float):
    """
    Распределяет данные моделируемых объктов по листам
    :param mas: масса
    :param electric_charge: электрический заряр
    :param x: координата x
    :param v_x: вектор по x
    :param y: координата y
    :param v_y: вектор по y
    """
    not_variable_balls.append(mas)
    not_variable_balls.append(electric_charge)
    variable.append(x)
    variable.append(v_x)
    variable.append(y)
    variable.append(v_y)

R = 10
N = 6
q = 1.1 * 10**(-5)
m = 1
v = 0.2

def get_xi(i): return R*np.cos((2*np.pi*i)/N)
def get_yi(i): return R*np.sin((2*np.pi*i)/N)

# Добавляем объекты моделирования
ball(m, -q, get_xi(0), 0, get_yi(0), v)
ball(m, +q, get_xi(1), -v, get_yi(1), 0)
ball(m, -q, get_xi(2), -v, get_yi(2), 0)
ball(m, +q, get_xi(3), 0, get_yi(3), -v)
ball(m, -q, get_xi(4), v, get_yi(4), 0)
ball(m, +q, get_xi(5), v, get_yi(5), 0)


# Вычисляем сколько всего мы моделируем объектов
N = int(len(not_variable_balls) / 2)

# Моделируем
sol = odeint(move_func, variable, t)


def solve_func(i: float, n: int, key: str):
    """
    :param i: время в которое мы берём координаты
    :param n: номер моделируемого объекта для которого мы получаем координаты
    :param key: ключь. Если key="point", то получам координаты для моделирования точьки
        в ином случае получае координаты для моделирования пути моделирукмого объекта
    :return x, y: n-го моделируемого элемента в i-е время
    """

    if key == "point":
        x = sol[i, n * 4 + 0]
        y = sol[i, n * 4 + 2]
    else:
        x = sol[:i, n * 4 + 0]
        y = sol[:i, n * 4 + 2]

    return x, y


fig, ax = plt.subplots()

# Лист графических элементов моделируемых объектов
# Переод = 2
# Данные одного моделируемого объекта: 0 = шар, 1 = путь
plots = []

# Создаём для каждего моделируемого объекта графические элементы
for i in range(N):
    # создаём рандомный цвет
    colors = np.random.rand(3, )

    # создаём графический элемент "шар"
    plot, = plt.plot([], [], 'o', c=colors, ms=5)
    plots.append(plot)

    # создаём графический элемент "лия"
    plot2, = plt.plot([], [], '-', c=colors)
    plots.append(plot2)


def animate(i):
    """
    Моделируем для каждего моделируемого объека графические элементы

    :param i: время в которое мы берём координаты
    """

    for j in range(N):
        plots[j * 2 + 0].set_data(solve_func(i, j, 'point'))
        plots[j * 2 + 1].set_data(solve_func(i, j, 'line'))


ani = FuncAnimation(fig,
                    animate,
                    frames=500,
                    interval=30)

plt.axis('equal')
edge = R*4
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

# plt.show()
ani.save("MyAnimTaskPRO.gif")
