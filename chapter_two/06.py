from pylab import linspace, plot, show


def fvalue(x_, n):
    return x_ ** (-n)


x = linspace(-1, 1, 100)
plot(x, fvalue(x, 1))
plot(x, fvalue(x, 2))
plot(x, fvalue(x, 3))
show()
