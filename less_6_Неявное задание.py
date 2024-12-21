	
import matplotlib.pyplot as plt
import numpy as np
 
 
def circle_plotter(R=10):
 
    x = np.arange(-2*R, 2*R, 0.1)
    y = np.arange(-2*R, 2*R, 0.1)
 
    # Переход к неявнозаданным координатам
    X, Y = np.meshgrid(x, y)
 
    fxy = X**2 + Y**2 - R**2  # Уравнение окружности
 
    # Команда рисования
    plt.contour(X, Y, fxy, levels=[0])
 
    plt.savefig('fig_4.png')
 
 
if __name__ == '__main__':
    circle_plotter()