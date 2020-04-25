from scipy.optimize import minimize
import matplotlib.pyplot as plt

skv = lambda x, y: sum([(i - j) ** 2 for i, j in zip(x, y)])


def determination_factor(x, y):
    ess = sum([(i - j) ** 2 for i, j in zip(x, y)])
    average_x = sum(x) / len(x)
    tss = sum([(i - average_x) ** 2 for i in x])
    R2 = 1 - ess / tss
    return R2


def func_minimaze(function, mas_x, mas_y, x0):
    min_func = lambda x: skv(mas_y, [function(i, x) for i in mas_x])

    # metods = ['Nelder-Mead', 'Powell', 'CG', 'BFGS', 'Newton-CG', 'L-BFGS-B', 'TNC',
    #           'COBYLA', 'SLSQP', 'trust-constr', 'dogleg', 'trust-ncg', 'trust-exact',
    #           'trust-krylov']

    res = minimize(min_func, x0, method='Powell',
                   options={'maxiter': 1000000, 'xtol': 0.000000001, 'ftol': 0.000000001})

    print(res.x)

    return res.x


def get_mas(function, x, mas_x):
    mas_z = [function(i, x) for i in mas_x]
    return mas_z


def draw_chart(mas_x, mas_y, mas_z, word):
    fig = plt.figure()
    graph = [plt.plot(mas_x, mas_y, '-'), plt.plot(mas_x, mas_z, '-k')]
    grid1 = plt.grid(True)
    plt.legend(['time series', word])
    plt.show()
