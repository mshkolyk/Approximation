import matplotlib.pyplot as plt
from scipy.optimize import minimize
import functions

file = open("data1.txt", 'r')
data = file.read()
m = data.split('\n')

mas_x = [float(i.split()[0]) for i in m]
mas_y = [float(i.split()[1]) for i in m]

x0 = [1.3, 0.7]


def func(x):
    return sum([(i - (x[0] * j + x[1])) ** 2 for i, j in zip(mas_y, mas_x)])


res = minimize(func, x0)
print(res.x)

fig = plt.figure()
graph = [plt.plot(mas_x, mas_y, '-'), plt.plot(mas_x, [res.x[0] * i + res.x[1] for i in mas_x], '-')]
grid1 = plt.grid(True)
plt.show()

print(functions.determination_factor(mas_y, [res.x[0] * i + res.x[1] for i in mas_x]))
print(mas_y)
