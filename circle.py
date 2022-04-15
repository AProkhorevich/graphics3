from matplotlib import pyplot as plt
import matplotlib
from shared import movePoint


def circle():
    centre = [float(x)
              for x in input("Enter the center of the circle:\n").split()]
    # Перенос в начало координат
    dx = centre[0]
    dy = centre[1]
    # подвинули в центр
    movePoint(centre, -dx)
    movePoint(centre, 0, -dy)

    R = float(input("Enter the radius of the circle:\n"))
    d = 1 - R
    # начальный пиксель
    x = 0
    y = R
    # массив пикселей
    X = [x]
    Y = [y]

    # рисуем круг
    c = plt.Circle(centre, R, color='r', fill=False)
    ax = plt.gca()
    ax.add_patch(c)
    # Алгоритм
    while x < y:
        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * x - 2 * y + 5
            y -= 1
        x += 1
        X.append(x)
        Y.append(y)

    # Отражение точек
    # иксы 1/8
    tmp = list(X)
    # исксы 1/4
    X.extend(Y)
    # игреки 1/4
    Y.extend(tmp)
    # остальные четверти
    X1 = X.copy()
    X2 = X.copy()
    X3 = X.copy()
    Y1 = Y.copy()
    Y2 = Y.copy()
    Y3 = Y.copy()
    # отражаем четверти
    # певрую по игреку
    # вторую по иксу
    # третью по икс-игреку
    for i in range(len(X)):
        X1[i] = -X1[i]
        Y2[i] = -Y2[i]
        X3[i] = -X3[i]
        Y3[i] = -Y3[i]

    # собираем круг
    Xe = X + X1 + X2 + X3
    Ye = Y + Y1 + Y2 + Y3

    # возвращаем из начала координат
    # в заданную точку центра окружности
    for i in range(len(Xe)):
        Xe[i] += dx
        Ye[i] += dy

    plt.title('Алгоритмы Брезенхема растеризации отрезка и окружности')
    fig = plt.figure(1)
    ax = fig.gca()
    locatorX = matplotlib.ticker.MultipleLocator(base=1)
    locatorY = matplotlib.ticker.MultipleLocator(base=1)
    ax.xaxis.set_major_locator(locatorX)
    ax.yaxis.set_major_locator(locatorY)
    ax.grid()
    ax.scatter(Xe, Ye)
    m = abs(max(centre)) + (2*R)
    # plt.xlim(-1*m, m)
    # plt.ylim(-1*m, m)
    plt.axis('equal')

    plt.show()


if __name__ == '__main__':
    circle()
