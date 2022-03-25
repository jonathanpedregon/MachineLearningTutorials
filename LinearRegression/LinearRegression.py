# https://machinelearningmastery.com/implement-simple-linear-regression-scratch-python/

def mean(values):
    return sum(values) / float(len(values))


def variance(values, mean):
    return sum([(x - mean) ** 2] for x in values)


dataset = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]
x = [row[0] for row in dataset]
y = [row[1] for row in dataset]
mean_x, mean_y = mean(x), mean(y)
var_x, var_y = variance(x, mean_x), variance(y, mean_y)
print('x stats: mean=%.3f variance=%.3f' % (mean_x, var_x))
print('y stats: mean=%.3f variance=%.3f' % (mean_y, var_y))
