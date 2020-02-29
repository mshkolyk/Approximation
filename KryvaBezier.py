import matplotlib.pyplot as plt
import Point2


def RecursBezier(mass, t):
    if len(mass) > 2:
        return RecursBezier(mass[:-1], t) * (1 - t) + RecursBezier(mass[1:], t) * t
    else:
        return mass[0] * (1 - t) + mass[1] * t


def BezierGrafik(mass0):
    mass1 = []
    for i in mass0:
        mass1.append(Point2.Point2(i[0], i[1]))

    n = 100

    mass = []

    for i in range(n):
        t = 1 * i / n
        mass.append(RecursBezier(mass1, t))

    mass_x1, mass_y1 = [], []
    for i in mass0:
        mass_x1.append(i[0])
        mass_y1.append(i[1])

    mass_x, mass_y = [], []
    for point in mass:
        # plt.scatter(point.x, point.y)
        mass_x.append(point.x)
        mass_y.append(point.y)

    fig = plt.figure()
    graph = plt.plot(mass_x, mass_y, 'b-', linewidth=3)
    graph1 = plt.plot(mass_x1, mass_y1, 'k--', linewidth=2)

    for k, point in enumerate(mass1):
        plt.scatter(point.x, point.y)
        text1 = plt.text(point.x*1.02, point.y*1.02, '  P' + str(k), fontsize=14)

    grid1 = plt.grid(True)  # линии вспомогательной сетки
    plt.show()

    # save(name='pic_2_1', fmt='pdf')
    # save(name='pic_2_1', fmt='png')


mass = [[-1.0, 0.0], [-0.5, 1], [1.0, 1.0], [0.5, 0.5], [1, 0.7]]
BezierGrafik(mass)
