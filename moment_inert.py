def calc_moment_inert(x, y):
    """
    Рассчитывает момент инерции плоской фигуры относительно оси,
    перпендикулярной плоскости фигуры и проходящей через начало координат.
    
    :param x: список X-координат вершин
    :param y: список Y-координат вершин
    :return: момент инерции I
    """
    n = len(x)
    if n < 3:
        return 0.0

    I = 0.0
    for i in range(n):
        xi, yi = x[i], y[i]
        xj, yj = x[(i + 1) % n], y[(i + 1) % n]
        cross = xi * yj - xj * yi
        mag_sq = xi**2 + yi**2 + xi*xj + yi*yj + xj**2 + yj**2
        I += cross * mag_sq

    I *= 1 / 12
    return abs(I)