import approximation_functions as af

file = open("data1.txt", 'r')
data = file.read()
m = data.split('\n')

mas_x = [float(i.split()[0]) for i in m]
mas_y = [float(i.split()[1]) for i in m]

# af.linear(mas_x, mas_y)
# af.exponential_decline(mas_x, mas_y)
# af.harmonic_decline(mas_x, mas_y) #
# af.hyperbolic_decline(mas_x, mas_y) #
# af.bleasdale(mas_x, mas_y)
# af.farazdaghi_harris(mas_x, mas_y)
# af.reciprocal(mas_x, mas_y)
# af.reciprocal_quadratic(mas_x, mas_y)
# af.reciprocal_yd(mas_x, mas_y)
# af.reciprocal_quadratic_yd(mas_x, mas_y)
# af.exponential_plus_linear(mas_x, mas_y)
# af.logistic(mas_x, mas_y)
# af.weibull_model(mas_x, mas_y)
# for i in range(6, 7):
#     af.polinom(mas_x, mas_y, i)

# af.ratkowsky_model(mas_x, mas_y)
af.mmf(mas_x, mas_y)