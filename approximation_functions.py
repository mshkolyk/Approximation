import functions as f
from math import exp


def linear(mas_x, mas_y):
    print("\nlinear")
    function = lambda i, x: x[0] * i + x[1]

    res = f.func_minimaze(function, mas_x, mas_y)
    mas_z = f.get_mas(function, res, mas_x)

    f.draw_chart(mas_x, mas_y, mas_z, 'linear approximation')

    print(f.determination_factor(mas_y, mas_z))


def exponential_decline(mas_x, mas_y):
    print("\nexponential_decline")

    function = lambda i, x: x[0] * exp(-i / x[1])

    res = f.func_minimaze(function, mas_x, mas_y)
    mas_z = f.get_mas(function, res, mas_x)

    f.draw_chart(mas_x, mas_y, mas_z, 'exponential decline approximation')

    print("R2 = ", f.determination_factor(mas_y, mas_z))
