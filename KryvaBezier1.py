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

    mass_x, mass_y = [], []
    fig = plt.figure()

    for point in mass:
        # plt.scatter(point.x, point.y)
        mass_x.append(point.x)
        mass_y.append(point.y)

    graph1 = plt.plot(mass_x, mass_y)

    for k, point in enumerate(mass1):
        plt.scatter(point.x, point.y)
        text1 = plt.text(point.x, point.y, '  P' + str(k))

    grid1 = plt.grid(True)  # линии вспомогательной сетки
    plt.show()

    # save(name='pic_2_1', fmt='pdf')
    # save(name='pic_2_1', fmt='png')

file = open("d.txt", 'r')
a = file.read()
m = a.split('\n')

##mass = []
##for i in m:
##    j = i.split('\t')
##    mass.append([float(j[0]), float(j[1])])
    
mass = [[-1.0, 0.0], [-0.5, 1], [1.0, 1.2], [0.5, 0.5], [2.5, 1]]
BezierGrafik(mass)

x = 5 if 0 else 6 
print(x)
