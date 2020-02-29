import matplotlib.pyplot as plt
import Point2
import numpy
import time


def recBSpline(x, t, i, k):

    if k==0:
        return 1 if x[i]<=t<x[i+1] else 0
    else:
        f1 = 0 if x[i+k] == x[i] else (t-x[i])*recBSpline(x, t, i, k-1)/(x[i+k] - x[i])
        f2 = 0 if x[i+k+1] == x[i+1] else (x[i+k+1]-t)*recBSpline(x, t, i+1, k-1)/(x[i+k+1] - x[i+1])
        return f1 + f2

#_____________________________ 
    
def BSpline(mas_x, mas_y, k):

    t1 = time.time()
    
    n = len(mas_x) - 1
    
    mas = []
    for i in range(n+k+1):
        mas.append(0 if 0<=i<k else i-k+1 if k<=i<=n else n-k+2)
        
    x = []
    y = []
    deviation = 0
    
    for t in numpy.arange(0, n-k+2, 0.01):
        s1, s2 = 0.0, 0.0
        for i in range(n+1):
            z = recBSpline(mas, t, i, k-1)
            s1 += mas_x[i]*z
            s2 += mas_y[i]*z

##        deviation = y - mas_y[
        x.append(s1)
        y.append(s2)

    deviation = deviation_func(mas_x, mas_y, y)
    print("number =", n+1, "| k =", k, "| time =", time.time()-t1, "| deviation =", deviation)

    return x, y


def deviation_func(mas_x, mas_y, y):
    max_deviation = 0
    for i in range(len(mas_y)):
        deviation = abs(mas_y[i]-y[i])
        if deviation > max_deviation:
            max_deviation = deviation
    return deviation
        

def drawGrafik(mas_x, mas_y, mas):
    fig = plt.figure()
    
    graph = [plt.plot(mas_x, mas_y, '-k')]
    for i in mas:
        graph.append(plt.plot(i[0], i[1], '--'))

    grid1 = plt.grid(True)
    plt.show()
    
#_____________________________
    
mas_x = [-1.0, -0.5, 1.0, 0.5, 2.5, 3]
mas_y = [0.1, 1.0, 1.2, 0.5, 1, 2]

##x, y = BSpline(mas_x, mas_y, 4)
##drawGrafik(mas_x, mas_y, [[x,y]])

file = open("d.txt", 'r')
a = file.read()
m = a.split('\n')

mas_x, mas_y = [], []
for i in m:
    j = i.split('\t')
    mas_x.append(int(j[0]))
    mas_y.append(float(j[1]))

k = 2

mas = []
for i in range(k, 6):
    mas.append(BSpline(mas_x, mas_y, i))

drawGrafik(mas_x, mas_y, mas)
