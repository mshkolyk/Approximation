import approximation_functions as af

file = open("data1.txt", 'r')
data = file.read()
m = data.split('\n')

mas_x = [float(i.split()[0]) for i in m]
mas_y = [float(i.split()[1]) for i in m]

af.linear(mas_x, mas_y)
af.exponential_decline(mas_x, mas_y)