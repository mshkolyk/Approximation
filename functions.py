def determination_factor(x, y):
    ess = sum([(i - j) ** 2 for i, j in zip(x, y)])
    average_x = sum(x) / len(x)
    tss = sum([(i - average_x) ** 2 for i in x])
    R2 = 1 - ess / tss
    return R2