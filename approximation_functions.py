import functions as f
from math import exp, log, sin, cos


def linear(mas_x, mas_y):
    print("\nlinear")
    function = lambda i, x: x[0] * i + x[1]

    res = f.func_minimaze(function, mas_x, mas_y, [1, 1])
    mas_z = f.get_mas(function, res, mas_x)

    f.draw_chart(mas_x, mas_y, mas_z, 'linear approximation')

    print('R2 =', f.determination_factor(mas_y, mas_z))


def polinom(k):
    def polinom(mas_x, mas_y):
        print("\npolinom", k)

        function = lambda i, x: sum([x[j] * (i ** j) for j in range(k + 1)])
        x0 = [0 for _ in range(k + 1)]

        res = f.func_minimaze(function, mas_x, mas_y, x0)
        mas_z = f.get_mas(function, res, mas_x)

        f.draw_chart(mas_x, mas_y, mas_z, 'polinom ' + str(k) + ' approximation')

        print('R2 =', f.determination_factor(mas_y, mas_z))

    return polinom

# Decline models
def exponential_decline(mas_x, mas_y):
    print("\nexponential decline")

    function = lambda i, x: x[0] * exp(-i / x[1])

    res = f.func_minimaze(function, mas_x, mas_y, [1, 1])
    mas_z = f.get_mas(function, res, mas_x)

    f.draw_chart(mas_x, mas_y, mas_z, 'exponential decline approximation')

    print("R2 =", f.determination_factor(mas_y, mas_z))


def harmonic_decline(mas_x, mas_y):
    print("\nharmonic decline")

    function = lambda i, x: x[0] / (1 + i / x[1])

    res = f.func_minimaze(function, mas_x, mas_y, [0, 1])
    mas_z = f.get_mas(function, res, mas_x)

    f.draw_chart(mas_x, mas_y, mas_z, 'harmonic decline approximation')

    print("R2 =", f.determination_factor(mas_y, mas_z))


def hyperbolic_decline(mas_x, mas_y):
    print("\nhyperbolic decline")

    function = lambda i, x: x[0] * (1 + x[2] * i / x[1]) ** (-1 / x[2])

    res = f.func_minimaze(function, mas_x, mas_y, [0, 0, -1])
    mas_z = f.get_mas(function, res, mas_x)

    f.draw_chart(mas_x, mas_y, mas_z, 'hyperbolic decline approximation')

    print("R2 =", f.determination_factor(mas_y, mas_z))


# Yield-Spacing models
def bleasdale(mas_x, mas_y):
    print("\nbleasdale")

    function = lambda i, x: (x[0] + x[1] * i) ** (-1 / x[2])

    res = f.func_minimaze(function, mas_x, mas_y, [1, 1, 1])
    mas_z = f.get_mas(function, res, mas_x)

    f.draw_chart(mas_x, mas_y, mas_z, 'bleasdale approximation')

    print("R2 =", f.determination_factor(mas_y, mas_z))


def farazdaghi_harris(mas_x, mas_y):
    print("\nfarazdaghi_harris")

    function = lambda i, x: 1 / (x[0] + x[1] * (i ** x[2]))

    res = f.func_minimaze(function, mas_x, mas_y, [1, 1, 1])
    mas_z = f.get_mas(function, res, mas_x)

    f.draw_chart(mas_x, mas_y, mas_z, 'farazdaghi-harris approximation')

    print("R2 =", f.determination_factor(mas_y, mas_z))


def reciprocal(mas_x, mas_y):
    print("\nreciprocal")

    function = lambda i, x: 1 / (x[0] + x[1] * i)

    res = f.func_minimaze(function, mas_x, mas_y, [1, 0])
    mas_z = f.get_mas(function, res, mas_x)

    f.draw_chart(mas_x, mas_y, mas_z, 'reciprocal approximation')

    print("R2 =", f.determination_factor(mas_y, mas_z))


def reciprocal_quadratic(mas_x, mas_y):
    print("\nreciprocal_quadratic")

    function = lambda i, x: 1 / (x[0] + x[1] * i + x[2] * (i ** 2))

    res = f.func_minimaze(function, mas_x, mas_y, [1, 0, 0])
    mas_z = f.get_mas(function, res, mas_x)

    f.draw_chart(mas_x, mas_y, mas_z, 'reciprocal_quadratic approximation')

    print("R2 =", f.determination_factor(mas_y, mas_z))


# Yield-Density models
def reciprocal_yd(mas_x, mas_y):
    print("\nreciprocal_yd")

    function = lambda i, x: i / (x[0] + x[1] * i)

    res = f.func_minimaze(function, mas_x, mas_y, [1, 0])
    mas_z = f.get_mas(function, res, mas_x)

    f.draw_chart(mas_x, mas_y, mas_z, 'reciprocal_yd approximation')

    print("R2 =", f.determination_factor(mas_y, mas_z))


def reciprocal_quadratic_yd(mas_x, mas_y):
    print("\nreciprocal_quadratic_yd")

    function = lambda i, x: i / (x[0] + x[1] * i + x[2] * (i ** 2))

    res = f.func_minimaze(function, mas_x, mas_y, [1, 0, 0])
    mas_z = f.get_mas(function, res, mas_x)

    f.draw_chart(mas_x, mas_y, mas_z, 'reciprocal_quadratic_yd approximation')

    print("R2 =", f.determination_factor(mas_y, mas_z))


def exponential_plus_linear(mas_x, mas_y):
    print("\nexponential_plus_linear")

    function = lambda i, x: x[0] + x[1] * (x[3] ** i) + x[2] * i

    res = f.func_minimaze(function, mas_x, mas_y, [1, 1, 0, 0])
    mas_z = f.get_mas(function, res, mas_x)

    f.draw_chart(mas_x, mas_y, mas_z, 'exponential plus linear approximation')

    print("R2 =", f.determination_factor(mas_y, mas_z))


# sigmoidal models
def logistic(mas_x, mas_y):
    print("\nlogistic")

    function = lambda i, x: x[0] / (1 + x[1] * exp(-x[2] * i))

    res = f.func_minimaze(function, mas_x, mas_y, [1, 1, 0])
    mas_z = f.get_mas(function, res, mas_x)

    f.draw_chart(mas_x, mas_y, mas_z, 'logistic approximation')

    print("R2 =", f.determination_factor(mas_y, mas_z))


def weibull_model(mas_x, mas_y):
    print("\nweibull_model")

    function = lambda i, x: x[0] - x[1] * exp(-x[2] * (i ** x[3]))

    res = f.func_minimaze(function, mas_x, mas_y, [1, -1, -1, -1])
    mas_z = f.get_mas(function, res, mas_x)

    f.draw_chart(mas_x, mas_y, mas_z, 'weibull model approximation')

    print("R2 =", f.determination_factor(mas_y, mas_z))


def ratkowsky_model(mas_x, mas_y):
    print("\nratkowsky_model")

    function = lambda i, x: x[0] / (1 + exp(x[1] - x[2] * i))

    res = f.func_minimaze(function, mas_x, mas_y, [1, 1, 0])
    mas_z = f.get_mas(function, res, mas_x)

    f.draw_chart(mas_x, mas_y, mas_z, 'ratkowsky model approximation')

    print("R2 =", f.determination_factor(mas_y, mas_z))


def mmf(mas_x, mas_y):
    print("\nmmf")

    function = lambda i, x: (x[0] * x[1] + x[2] * (i ** x[3])) / (x[1] + i ** x[3])

    res = f.func_minimaze(function, mas_x, mas_y, [1, 0, 0, 0])
    mas_z = f.get_mas(function, res, mas_x)

    f.draw_chart(mas_x, mas_y, mas_z, 'mmf approximation')

    print("R2 =", f.determination_factor(mas_y, mas_z))


# ...
def exponential(mas_x, mas_y):
    print("\nexponential")

    function = lambda i, x: x[0] * exp(x[1] * i)

    res = f.func_minimaze(function, mas_x, mas_y, [1, 0])
    mas_z = f.get_mas(function, res, mas_x)

    f.draw_chart(mas_x, mas_y, mas_z, 'exponential approximation')

    print("R2 =", f.determination_factor(mas_y, mas_z))


def modified_exponential(mas_x, mas_y):
    print("\nmodified_exponential")

    function = lambda i, x: x[0] * exp(x[1] / i)

    res = f.func_minimaze(function, mas_x, mas_y, [1, 0])
    mas_z = f.get_mas(function, res, mas_x)

    f.draw_chart(mas_x, mas_y, mas_z, 'modified exponential approximation')

    print("R2 =", f.determination_factor(mas_y, mas_z))


def vapor_pressure_model(mas_x, mas_y):
    print("\nvapor_pressure_model")

    function = lambda i, x: exp(x[0] + x[1] / i + x[2] * log(i))

    res = f.func_minimaze(function, mas_x, mas_y, [1, 0, 1])
    mas_z = f.get_mas(function, res, mas_x)

    f.draw_chart(mas_x, mas_y, mas_z, 'vapor pressure model approximation')

    print("R2 =", f.determination_factor(mas_y, mas_z))


def vapor_pressure_model(mas_x, mas_y):
    print("\nvapor_pressure_model")

    function = lambda i, x: exp(x[0] + x[1] / i + x[2] * log(i))

    res = f.func_minimaze(function, mas_x, mas_y, [1, 0, 1])
    mas_z = f.get_mas(function, res, mas_x)

    f.draw_chart(mas_x, mas_y, mas_z, 'vapor pressure model approximation')

    print("R2 =", f.determination_factor(mas_y, mas_z))


def sinusoidal(mas_x, mas_y):
    print("\nsinusoidal")

    function = lambda i, x: x[0] + x[1] * cos(x[2] * i + x[3])

    res = f.func_minimaze(function, mas_x, mas_y, [1, 1, 0, 1])
    mas_z = f.get_mas(function, res, mas_x)

    f.draw_chart(mas_x, mas_y, mas_z, 'sinusoidal approximation')

    print("R2 =", f.determination_factor(mas_y, mas_z))


def rational_model(mas_x, mas_y):
    print("\nrational_model")

    function = lambda i, x: (x[0] + x[1] * i) / (1 + x[2] * i + x[3] * (i ** 2))

    res = f.func_minimaze(function, mas_x, mas_y, [1, 1, 0, 0])
    mas_z = f.get_mas(function, res, mas_x)

    f.draw_chart(mas_x, mas_y, mas_z, 'rational model approximation')

    print("R2 =", f.determination_factor(mas_y, mas_z))


def steinhart_hart_equation(mas_x, mas_y):
    print("\nsteinhart_hart_equation")

    function = lambda i, x: 1 / (x[0] + x[1] * log(i) + x[2] * (log(i) ** 3))

    res = f.func_minimaze(function, mas_x, mas_y, [1, 0, 0])
    mas_z = f.get_mas(function, res, mas_x)

    f.draw_chart(mas_x, mas_y, mas_z, 'steinhart hart equation approximation')

    print("R2 =", f.determination_factor(mas_y, mas_z))


def truncated_fourier_series(mas_x, mas_y):
    print("\nsteinhart hart equation")

    function = lambda i, x: x[0]*cos(i+x[3])+x[1]*cos(2*i+x[3])+x[2]*cos(3*i+x[3])

    res = f.func_minimaze(function, mas_x, mas_y, [0, 0, 0, 1])
    mas_z = f.get_mas(function, res, mas_x)

    f.draw_chart(mas_x, mas_y, mas_z, 'truncated fourier series approximation')

    print("R2 =", f.determination_factor(mas_y, mas_z))