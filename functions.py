from scipy.optimize import minimize
import matplotlib.pyplot as plt

skv = lambda x, y: sum([(i - j) ** 2 for i, j in zip(x, y)])


def determination_factor(x, y):
    ess = sum([(i - j) ** 2 for i, j in zip(x, y)])
    average_x = sum(x) / len(x)
    tss = sum([(i - average_x) ** 2 for i in x])
    R2 = 1 - ess / tss
    return R2


def func_minimaze(function, mas_x, mas_y, x0, all=0):
    min_func = lambda x: skv(mas_y, [function(i, x) for i in mas_x])

    if all:
        methods = ['Nelder-Mead', 'Powell', 'CG', 'BFGS', 'L-BFGS-B', 'TNC',
                   'COBYLA', 'SLSQP', 'trust-constr']
        # error_methods = ['Newton-CG', 'dogleg', 'trust-ncg', 'trust-exact', 'trust-krylov']

        all_res = {}
        for method in methods:
            if method in ['Nelder-Mead', 'Powell', 'TNC']:
                options = {'maxiter': 1000000, 'xtol': 0.000000001, 'ftol': 0.000000001}
            else:
                options = {}
            all_res[method] = {'res': minimize(min_func, x0, method=method, options=options).x}
            all_res[method]['r2'] = determination_factor(mas_y, get_mas(function, all_res[method]['res'], mas_x))

        search_method = 'Powell'
        for method in methods:
            try:
                if all_res[method]['r2'] > all_res[search_method]['r2']:
                    search_method = method
            except:
                pass

        return all_res[search_method]['res']

    else:
        res = minimize(min_func, x0, method='Powell',
                       options={'maxiter': 1000000, 'xtol': 0.000000001, 'ftol': 0.000000001})

        return res.x


def get_mas(function, x, mas_x):
    mas_z = [function(i, x) for i in mas_x]
    return mas_z


def draw_chart(mas_x, mas_y, mas_z, word):
    fig = plt.figure()
    graph = [plt.plot(mas_x, mas_y, '-'), plt.plot(mas_x, mas_z, '-k')]
    grid1 = plt.grid(True)
    plt.legend(['time series', word])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
