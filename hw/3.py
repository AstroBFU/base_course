import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

def circle_plotter(a=1,b=0.5):

    x = np.arange(-2*a, 2*b, 14)
    y = np.arange(-2*a, 2*b, 16)

    # Переход к неявнозаданным координатам
    X, Y = np.meshgrid(x, y)

    fxy = X**2 + Y**2 - radius**2  # Уравнение окружности

    # Команда рисования
    plt.contour(X, Y, fxy, levels=[0])
    plt.axis('equal')

    plt.savefig('fig_4.png')


if __name__ == '__main__':
    circle_plotter()