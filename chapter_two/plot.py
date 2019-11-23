from pylab import *

x = linspace(-5, 5, 1000)


def function(arg):
    return exp(-arg ** 2)


plot(x, function(x))

show()


def derivative(func, x, h):
    return (func(x + h) - func(x - h)) / (2 * h)


plot(x, derivative(function, x, .001))

show()
