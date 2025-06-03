def calc_center_mass(x, y):
    """
    Вычисляет центр масс многоугольника по координатам его вершин.
    :param x: Список x-координат вершин.
    :param y: Список y-координат вершин.
    :return: Координаты центра масс (Cx, Cy).
    """
    n = len(x)
    A = 0.0
    Cx = 0.0
    Cy = 0.0

    for i in range(n):
        # Циклический индекс
        j = (i + 1) % n
        # Вычисление детерминанта (удвоенная площадь треугольника)
        factor = x[i] * y[j] - x[j] * y[i]
        A += factor
        Cx += (x[i] + x[j]) * factor
        Cy += (y[i] + y[j]) * factor

    A *= 0.5
    Cx /= (6.0 * A)
    Cy /= (6.0 * A)

    return Cx, Cy