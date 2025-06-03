from tkinter import *
import matplotlib.pyplot as plt
import scipy.interpolate as sc
from scipy.integrate import odeint
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Для встраивания графика в Tkinter
from matplotlib.animation import FuncAnimation
from PIL import Image, ImageTk

from const import *
from class_paint import Paint
from center_mass import calc_center_mass
from moment_inert import calc_moment_inert

x = []
y = []
omega = 0
omega_array = []
time_array = []

alpha = np.pi/4

def ray_segment_intersection(ray_origin, ray_dir, segment_p1, segment_p2):
    """
    ray_origin — начальная точка луча (x, y)
    ray_dir — направление луча (dx, dy)
    segment_p1, segment_p2 — концы отрезка
    Возвращает True, если луч пересекает отрезок
    """
    # Работаем с numpy
    p0 = np.array(ray_origin)
    d = np.array(ray_dir)
    p1 = np.array(segment_p1)
    p2 = np.array(segment_p2)

    e1 = p1 - p0
    e2 = p2 - p1
    cross_d_e2 = d[0] * e2[1] - d[1] * e2[0]
    if abs(cross_d_e2) < 1e-10:
        return False  # Коллинеарны или параллельны

    t = (e1[0] * e2[1] - e1[1] * e2[0]) / cross_d_e2
    u = (e1[0] * d[1] - e1[1] * d[0]) / cross_d_e2

    return t >= 0 and 0 <= u <= 1

def btn_func():
    # Получаем значение температуры из текстового поля
    try:
        global lumin, albedo, a, ro, tau
        lumin = float(lumin_entry.get())
        albedo = float(albedo_entry.get())
        a = float(a_entry.get())
        ro = float(ro_entry.get())
        tau = int(tau_entry.get())
    except ValueError:
        return

    # Проверка на наличие данных
    global x, y
    if len(x) < 3 or len(y) < 3:
        return

    # Закрываем текущее окно рисования
    app.destroy()

    # Создаем фигуру matplotlib
    fig, ax = plt.subplots(figsize=(9, 6))

    # Построение нарисованного объекта
    x.append(x[0])  # Замыкаем фигуру
    y.append(y[0])
    x_arr = np.array(x)
    y_arr = np.array(y)

    # Аппроксимация нарисованного объекта
    step = 1000
    mytck, myu = sc.splprep([x_arr, y_arr])
    global xnew, ynew
    xnew, ynew = sc.splev(np.linspace(0, 1, step), mytck)

    # Вычисляем центр масс
    global Cx, Cy
    Cx, Cy = calc_center_mass(xnew, ynew)
    ax.scatter(0, 0, color='blue', zorder=5)

    xnew = np.array(xnew)
    ynew = np.array(ynew)
    xnew -= Cx
    ynew -= Cy

    # Расчёт момента инерции
    global moment_of_inertia
    moment_of_inertia = round(calc_moment_inert(xnew, ynew))

    
    ax.plot(xnew, ynew, 'black')
    plt.title("Ваш астероид!")

    # Встраиваем график в Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame1)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=BOTH, expand=True)

    button.destroy()

    global button_label
    button_label = Label(master=frame3, text="Корректно ли всё отображается?", bg="gray", fg="white")
    button_label.place(x=20, y=470)

    global button_new
    button_new = Button(master=frame3, text="Да!", command=anim_func)
    button_new.place(x=20, y=500)
    
def anim_func():
    button_label.destroy()
    button_new.destroy()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    root.geometry(f"1500x600+5+{h_window}")

    edge = 2*max(xnew)
    ax1.set_xlim(-edge, edge)
    ax1.set_ylim(-edge, edge)
    ax1.set_xlabel("Координаты по OX, м")
    ax1.set_ylabel("Координаты по OY, м")
    ax1.set_title("Движение астероида")

    ax2.set_xlim(0, 200)
    ax2.set_ylim(-0.5, 0.5)
    ax2.set_xlabel("Время, года")
    ax2.set_ylabel("Угловая скорость, °/час")
    ax2.set_title("Изменение ω")

    global asteroid
    asteroid, = ax1.plot([], [], '-', color='black')

    global omega_anim, omega_anim_lines
    omega_anim_lines, = ax2.plot([], [], '-', color='b')
    omega_anim, = ax2.plot([], [], 'o', color='red')
    
    global ani
    ani = FuncAnimation(fig, animate, frames=500, interval=60)

    plt.tight_layout()
    ani.save("anim_asteroid.gif")

    del ani
    ani = None

    show_gif()
    return

def show_gif():
    for widget in frame1.winfo_children():
        widget.destroy()

    gif = Image.open("anim_asteroid.gif")
    frames = []

    try:
        for i in range(gif.n_frames):
            gif.seek(i)
            frame = ImageTk.PhotoImage(gif.convert("RGBA"))
            frames.append(frame)

    except EOFError:
        pass

    label = Label(frame1)
    label.pack()

    def update(ind):
        frame = frames[ind]
        ind = (ind + 1) % len(frames)
        label.configure(image=frame)
        root.after(60, update, ind)

    root.after(0, update, 0)

def move_func(t):
    global xnew, ynew, omega, omega_array, time_array
    
    gamma = []
    beta_aray = []
    x_h_array = []
    y_h_array = []
    S_array = []
    time = 10**7

    # Разделение на участки с заданной точностью
    acc = 20
    step = 1000
    for i in range(0, step, acc):
        try:
            x_h = (xnew[i] + xnew[i+acc]) / 2
            y_h = (ynew[i] + ynew[i+acc]) / 2

            # Нормальный вектор (ненормированный)
            if xnew[0+acc] < xnew[0]:
                x_n = ynew[i+acc] - ynew[i]
                y_n = xnew[i] - xnew[i+acc]
            else:
                x_n = - ynew[i+acc] + ynew[i]
                y_n = - xnew[i] + xnew[i+acc]

            # Единичный нормальный вектор
            norm = np.sqrt(x_n**2 + y_n**2)
            X_n = x_n / norm
            Y_n = y_n / norm

            # Конец нормали (отложено от середины)
            scale = 20  # Длина нормали
            x_end = x_h + scale * X_n
            y_end = y_h + scale * Y_n

        except IndexError:
            x_h = (xnew[i] + xnew[0]) / 2
            y_h = (ynew[i] + ynew[0]) / 2

            # Нормальный вектор (ненормированный)
            if xnew[0+acc] < xnew[0]:
                x_n = ynew[0] - ynew[i]
                y_n = xnew[i] - xnew[0]
            else:
                x_n = - ynew[0] + ynew[i]
                y_n = - xnew[i] + xnew[0]

            # Единичный нормальный вектор
            norm = np.sqrt(x_n**2 + y_n**2)
            X_n = x_n / norm
            Y_n = y_n / norm

            # Конец нормали (отложено от середины)
            scale = 20  # Длина нормали
            x_end = x_h + scale * X_n
            y_end = y_h + scale * Y_n

        sun_dir = np.array([np.cos(alpha), np.sin(alpha)])

        is_in_shadow = False
        for j in range(0, step, acc):

            p1 = [xnew[j], ynew[j]]
            p2 = [xnew[(j + acc) % step], ynew[(j + acc) % step]]

            if ray_segment_intersection((x_h, y_h), sun_dir, p1, p2):
                is_in_shadow = True
                break

        if is_in_shadow == False: # Участок не в тени
        
            beta = np.arccos((x_end-x_h)/(np.sqrt((x_end-x_h)**2 + (y_end-y_h)**2)))
            if np.arcsin((y_end-y_h)/(np.sqrt((x_end-x_h)**2 + (y_end-y_h)**2)))<0:
                beta = - beta

            if beta >= 0:
                if beta >= alpha:
                    if beta - alpha < np.pi/2:
                        gamma.append(float(beta - alpha))
                        beta_aray.append(beta)
                        x_h_array.append(x_h)
                        y_h_array.append(y_h)
                        S_array.append(abs(y_n))
                else:
                    if alpha - beta < np.pi/2:
                        gamma.append(float(alpha - beta))
                        beta_aray.append(beta)
                        x_h_array.append(x_h)
                        y_h_array.append(y_h)
                        S_array.append(abs(y_n))
            else:
                if abs(beta) >= np.pi - alpha:
                    if 2*np.pi - abs(beta) - alpha < np.pi/2:
                        gamma.append(float(2*np.pi - abs(beta) - alpha))
                        beta_aray.append(beta)
                        x_h_array.append(x_h)   
                        y_h_array.append(y_h)
                        S_array.append(abs(y_n))
                else:
                    if alpha + abs(beta) < np.pi/2:
                        gamma.append(float(alpha + abs(beta)))
                        beta_aray.append(beta)
                        x_h_array.append(x_h)
                        y_h_array.append(y_h)
                        S_array.append(abs(y_n))

    dF = 2/3 * (1-albedo) * (lumin * lumin_son) / (4*np.pi*(a*ae)**2) * np.cos(gamma) / np.pi  / c
    M = 0
    for i in range(0, len(gamma)):
        if beta_aray[i] >= alpha:
            M += dF[i] * S_array[i] * np.sqrt((x_h_array[i])**2+(y_h_array[i])**2) 
        else:
            M -= dF[i] * S_array[i] * np.sqrt((x_h_array[i])**2+(y_h_array[i])**2)

    epsilon = M / (ro * moment_of_inertia)
    omega += epsilon*time
    omega = float(omega)
    omega_array.append(float(omega*180/np.pi*60*60))

    x_0 = np.array(xnew)
    y_0 = np.array(ynew)
    phi_0 = np.array(np.arccos(x_0/np.sqrt((x_0)**2+(y_0)**2)))
    for i in range(0, len(phi_0)):
        if np.array(np.arcsin(y_0/np.sqrt((x_0)**2+(y_0)**2)))[i]<0:
            phi_0[i] = - phi_0[i]
    r = np.array(np.sqrt((x_0)**2+(y_0)**2))

    phi = np.array(phi_0 + omega*time)
    x = np.array(r * np.cos(phi))
    y = np.array(r * np.sin(phi))

    time = time * len(omega_array)
    time_array.append(time/60/60/24/365)

    xnew, ynew = x,y

    return xnew, ynew, float(time/60/60/24/365), float(omega*180/np.pi*60*60), time_array, omega_array

def animate(i):
    if ani == None:
        raise ValueError()
    print(i)
    X, Y, Time, Omega, Time_array, Omega_array = move_func(t=i)

    asteroid.set_data(X, Y)

    omega_anim.set_data([Time], [Omega])
    omega_anim_lines.set_data([Time_array],[Omega_array])

    return asteroid, omega_anim, omega_anim_lines

# Размеры окна
w = 900
h = 600

root = Tk()
w_root = 1200
h_root = 600
w_window = root.winfo_screenwidth() // 2 - w_root // 2
h_window = root.winfo_screenheight() // 2 - h_root // 2
root.geometry(f"1200x600+{w_window}+{h_window}")
root.title("YORP-эффект")
root.resizable(width=False, height=False)

frame0 = Frame(master=root, width=w, height=h, bg="black")
frame0.pack(fill=BOTH, side=LEFT, expand=True)

frame1 = Frame(master=frame0)
frame1.pack(fill=BOTH, expand=True)

frame2 = Frame(master=root, width=2, bg="black")
frame2.pack(fill=Y, side=LEFT)

frame3 = Frame(master=root, width=200, bg="gray")
frame3.pack(fill=BOTH, side=LEFT, expand=True)

# Метка для текстового поля
lumin_label = Label(master=frame3, text="Светимость звезды (в св. Солнца):", bg="gray", fg="white")
lumin_label.place(x=20, y=50)

# Текстовое поле для ввода температуры
lumin_entry = Entry(master=frame3, width=15)
lumin_entry.place(x=20, y=80)

albedo_label = Label(master=frame3, text="Альбедо тела:", bg="gray", fg="white")
albedo_label.place(x=20, y=110)

albedo_entry = Entry(master=frame3, width=15)
albedo_entry.place(x=20, y=140)

a_label = Label(master=frame3, text="Большая полуось (а.е.):", bg="gray", fg="white")
a_label.place(x=20, y=170)

a_entry = Entry(master=frame3, width=15)
a_entry.place(x=20, y=200)

ro_label = Label(master=frame3, text="Плотность тела (кг/м:3):", bg="gray", fg="white")
ro_label.place(x=20, y=230)

ro_entry = Entry(master=frame3, width=15)
ro_entry.place(x=20, y=260)

tau_label = Label(master=frame3, text="Время моделирования (десятки тысяч лет):", bg="gray", fg="white")
tau_label.place(x=20, y=290)

tau_entry = Entry(master=frame3, width=15)
tau_entry.place(x=20, y=320)

button = Button(master=frame3, text="Сохранить!", command=btn_func)
button.place(x=20, y=500)

app = Paint(frame1, x, y)  # Передаем размеры окна
root.mainloop()
