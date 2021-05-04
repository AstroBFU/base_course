# -*- coding: utf-8 -*-
"""
Created on Tue May  4 18:21:42 2021

@author: admin
"""
import tkinter as tk 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
from scipy.integrate import odeint
from scipy.integrate import odeint


class Supernova:
    def __init__(self, R):
        
        self.M = 20 # Масса ядра в Солнечных массах
        self.R = 0.2  # Радиус ядра в Солнечных радиусах
        self.G = 6.67430 * 10**(-11)
        self.m_sun = 1.989*10**30
        self.R_sun = 696340*10**3
        self.R_shel = R # Радиус оболочки в солнечных радиусах
        
        self.T = 20000 # Время анимации в секундах (соответствует примерно реальному времени коллапса оболочки)
        self.n = 2000  # Число шагов / кадров

        self.tau = np.linspace(0,self.T,self.n) # Массив для одного временного шага

        self.N = 25 # Число частиц оболочки
        self.p = np.zeros((self.N,4)) # Массив для координат и скоростей всех точек

# Массивы для записи координат для итоговой анимации
        self.x = np.zeros((self.N,self.n))
        self.y = np.zeros((self.N,self.n))

        
        for i in range(self.N): # Цикл для расстоновки точек по кругу
            self.p[i,0], self.p[i,1], self.p[i,2], self.p[i,3] = self.R_shel*np.cos(2*np.pi*i/self.N), 0, self.R_shel*np.sin(2*np.pi*i/self.N), 0
            self.x[i,0], self.y[i,0] = self.p[i,0], self.p[i,2]

    def move_func(self, s, t):
        x, v_x, y, v_y = s

    # Система диф. уравнений на базе второго закона Ньютона
        self.g = self.G * self.m_sun * self.M / (self.R_sun**2*(x**2 + y**2))

        dxdt = v_x
        dv_xdt = - self.g * x / (self.R_sun * np.sqrt(x**2 + y**2))

        dydt = v_y
        dv_ydt = - self.g * y / (self.R_sun * np.sqrt(x**2 + y**2))

        return dxdt, dv_xdt, dydt, dv_ydt


    def collision(self, x1, vx1, y1, vy1, x2, vx2, y2, vy2, radius1, radius2, mass1, mass2, K):
        """Аргументы функции:
        x1,y1,vx1,vy1 - координаты и компоненты скорости 1-ой частицы
        x2,y2,vx2,vy2 - ... 2-ой частицы
        radius,mass1,mass2 - радиус частиц и их массы (массы разные можно задавать,
        радиус для простоты взят одинаковый)
        K - коэффициент восстановления (K=1 для абсолютного упругого удара, K=0
        для абсолютно неупругого удара, 0<K<1 для реального удара).
        В данном случае коэффициент ВАЖНО положить больше 1, чтобы учесть дополнительную
        кенетическую энергию, возникающую в результате взрыва.
        Функция возвращает компоненты скоростей частиц, рассчитанные по формулам для
        реального удара, если стокновение произошло. Если удара нет, то возвращаются
        те же значения скоростей, что и заданные в качестве аргументов.
        """
        r12 = np.sqrt((x1-x2)**2 + (y1-y2)**2) #расчет расстояния между центрами частиц
        # расчет модулей скоростей частиц
        v1 = np.sqrt(vx1**2 + vy1**2)
        v2 = np.sqrt(vx2**2 + vy2**2)
    
        #проверка условия на столкновение: расстояние должно быть меньше 2-х радиусов
        if r12 <= radius1 + radius2:
            '''вычисление углов движения частиц theta1(2), т.е. углов между
            направлением скорости частицы и положительным направлением оси X.
            Если частица  покоится, то угол считается равным нулю. Т.к. функция
            arccos имеет область значений от 0 до Pi, то в случае отрицательных
            y-компонент скорости для вычисления угла theta1(2) надо из 2*Pi
            вычесть значение arccos(vx/v)
            '''
            if v1!=0:
                theta1 = np.arccos(vx1 / v1)
            else:
                theta1 = 0
            if v2!=0:
                theta2 = np.arccos(vx2 / v2)
            else:
                theta2 = 0
            if vy1<0:
                theta1 = - theta1 + 2 * np.pi
            if vy2<0:
                theta2 = - theta2 + 2 * np.pi
    
            #вычисление угла соприкосновения.
            if (y1-y2)<0:
                phi = - np.arccos((x1-x2) / r12) + 2 * np.pi
            else:
                phi = np.arccos((x1-x2) / r12)
    
            # Пересчет  x-компоненты скорости первой частицы
            VX1 = v1 * np.cos(theta1 - phi) * (mass1 - K * mass2) \
            * np.cos(phi) / (mass1 + mass2)\
            + ((1 + K) * mass2 * v2 * np.cos(theta2 - phi))\
            * np.cos(phi) / (mass1 + mass2)\
            + K * v1 * np.sin(theta1 - phi) * np.cos(phi + np.pi / 2)
    
            # Пересчет y-компоненты скорости первой частицы
            VY1 = v1 * np.cos(theta1 - phi) * (mass1 - K * mass2) \
            * np.sin(phi) / (mass1 + mass2) \
            + ((1 + K) * mass2 * v2 * np.cos(theta2 - phi)) \
            * np.sin(phi) / (mass1 + mass2) \
            + K * v1 * np.sin(theta1 - phi) * np.sin(phi + np.pi / 2)
    
            # Пересчет x-компоненты скорости второй частицы
            VX2 = v2 * np.cos(theta2 - phi) * (mass2 - K * mass1) \
            * np.cos(phi) / (mass1 + mass2)\
            + ((1 + K) * mass1 * v1 * np.cos(theta1 - phi)) \
            * np.cos(phi) / (mass1 + mass2)\
            + K * v2 * np.sin(theta2 - phi) * np.cos(phi + np.pi / 2)
    
            # Пересчет y-компоненты скорости второй частицы
            VY2 = v2 * np.cos(theta2 - phi) * (mass2 - K * mass1) \
            * np.sin(phi) / (mass1 + mass2) \
            + ((1 + K) * mass1 * v1 * np.cos(theta1 - phi)) \
            * np.sin(phi) / (mass1 + mass2)\
            + K * v2 * np.sin(theta2 - phi) * np.sin(phi + np.pi / 2)
    
        else:
            #если условие столкновнеия не выполнено, то скорости частиц не пересчитываются
            VX1, VY1, VX2, VY2 = vx1,vy1,vx2,vy2
    
        return VX1, VY1, VX2, VY2

    def out(self):
        
        for k in range(self.n-1):
            t=[self.tau[k],self.tau[k+1]]
            for m in range(self.N):
                s0 = self.p[m,0], self.p[m,1], self.p[m,2], self.p[m,3]
                sol = odeint(self.move_func, s0, t)
    
                self.p[m,0] = sol[1,0]
                self.p[m,1] = sol[1,1]
                self.p[m,2] = sol[1,2]
                self.p[m,3] = sol[1,3]
    
            self.x[m,k+1], self.y[m,k+1] = self.p[m,0], self.p[m,2]
    
            self.res = self.collision(self.p[m,0],self.p[m,1],self.p[m,2],self.p[m,3], 0, 0, 0, 0, 0.01, 0.5, 0, 1, 2)
            
            
            self.p[m,1], self.p[m,3] = self.res[0], self.res[1]
            print(self.p)
        #return self.p
    
supernova_1 = Supernova(1)
print(supernova_1.out()[5,5])