import matplotlib.pyplot as plt
from pulp import *

file = open("data1.txt", 'r')
data = file.read()
m = data.split('\n')

mas_x = [float(i.split()[0]) for i in m]
mas_y = [float(i.split()[1]) for i in m]

# print(sum([pow(i - (1 * j + 1), 2) for i, j in zip(mas_y, mas_x)]))

prob = LpProblem("Problem", LpMinimize)

var_a = LpVariable('a', 0.1)
var_b = LpVariable('b')
var_skv = LpVariable('skv')

prob += var_skv == sum(
    [(i - (var_a * j + var_b))
     if i >= (var_a * j + var_b) else (var_a * j + var_b) - i
     for i, j in zip(mas_y, mas_x)])

prob += var_skv
prob.solve()

print("Status:", LpStatus[prob.status])

for v in prob.variables():
    print(v.name, "=", v.varValue)
    if v.name == 'a':
        a = v.varValue
    if v.name == 'b':
        b = v.varValue

fig = plt.figure()
graph = [plt.plot(mas_x, mas_y, '-'), plt.plot(mas_x, [a * i + b for i in mas_x], '-')]
grid1 = plt.grid(True)
plt.show()
