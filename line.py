from matplotlib import pyplot as plt
import matplotlib
from shared import movePoint


MOVE = 'moved'
REFLECT_OX = 'reflectedox'
REFLECT_OY = 'reflectedoy'
REFLECT_YX = 'reflectedyx'


def reflection(a):
    a.reverse()


def correct_angle(a, b):
    # проверка что прямая лежит под прямой y = x
    x = abs(a[0] - b[0])
    y = abs(a[1] - b[1])
    if -x + y <= 0:
        return True
    else:
        return False


def reflectionOX(a):
    a[1] = -a[1]


def reflectionOY(a):
    a[0] = -a[0]


def line():
    a = [int(x) for x in input("Enter point 1 (x y):\n").split()]
    b = [int(x) for x in input("Enter point 2 (x y):\n").split()]
    # иксовые координаты
    A = [a[0], b[0]]
    # игрековые
    B = [a[1], b[1]]
    modifications = []

    # геом преобразования
    if a[0] != 0 or a[1] != 0:
        # смещаем начало координат
        dx = -a[0]
        dy = -a[1]
        a = movePoint(a, dx, dy)
        b = movePoint(b, dx, dy)
        A1 = [a[0], b[0]]
        B1 = [a[1], b[1]]
        modifications.append({MOVE: (dx, dy)})

    # Если точка находится в III
    # отражаем по ОХ
    if a[1] < 0 or b[1] < 0:
        reflectionOX(a)
        reflectionOX(b)
        A2 = [a[0], b[0]]
        B2 = [a[1], b[1]]
        modifications.append({REFLECT_OX: 0})

    # Если точка находится в 2/4 или 3/4
    if a[0] < 0 or b[0] < 0:
        reflectionOY(a)
        reflectionOY(b)
        A3 = [a[0], b[0]]
        B3 = [a[1], b[1]]
        modifications.append({REFLECT_OY: 0})

    if not correct_angle(a, b):
        reflection(a)
        reflection(b)
        A4 = [a[0], b[0]]
        B4 = [a[1], b[1]]
        modifications.append({REFLECT_YX: 0})

    # Получаем точки (алгоритм)
    d = (b[1] - a[1]) - 0.5 * (b[0] - a[0])
    X = [a[0]]
    Y = [a[1]]
    y = a[1]
    for x in range(a[0], b[0]):
        X.append(x + 1)
        if d <= 0:
            d += b[1] - a[1]
        else:
            d += b[1] - a[1] - b[0] + a[0]
            y += 1
        Y.append(y)
    print(X)
    print(Y)

    finalPoints = [[x, y] for x, y in zip(X, Y)]

    # откатываем операции в обратном порядке
    print(modifications)
    for i in modifications[::-1]:
        for h in i:
            if h == REFLECT_YX:
                for j in finalPoints:
                    reflection(j)
            elif h == REFLECT_OY:
                for j in finalPoints:
                    reflectionOY(j)
            elif h == REFLECT_OX:
                for j in finalPoints:
                    reflectionOX(j)
            elif h == MOVE:
                for j in range(len(finalPoints)):
                    finalPoints[j] = movePoint(
                        finalPoints[j], -i[MOVE][0], -i[MOVE][1])

    xfinal = []
    yfinal = []
    for i in finalPoints:
        xfinal.append(i[0])
        yfinal.append(i[1])

    fig = plt.figure(1)
    ax = fig.gca()
    locatorX = matplotlib.ticker.MultipleLocator(base=1)
    locatorY = matplotlib.ticker.MultipleLocator(base=1)
    ax.xaxis.set_major_locator(locatorX)
    ax.yaxis.set_major_locator(locatorY)
    ax.grid()
    ax.plot(A, B)
    try:
        ax.plot(A1, B1, c='b')
    except NameError:
        pass
    try:
        ax.plot(A2, B2, c='g')
    except NameError:
        pass
    try:
        ax.plot(A3, B3, c='y')
    except NameError:
        pass
    try:
        ax.plot(A4, B4, c='r')
    except NameError:
        pass
    ax.scatter(X, Y)
    ax.scatter(xfinal, yfinal)
    plt.axis('equal')
    plt.show()


if __name__ == '__main__':
    line()
