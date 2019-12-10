from pylab import sin, linspace, plot, show, legend


def gvalue(x, n):
    return sin(x) / x ** n


x = linspace(-5, 5)
plot(x, gvalue(x, 1), label='sin(x)/x')
plot(x, gvalue(x, 2), label='sin(x)/x^2')
plot(x, gvalue(x, 3), label='sin(x)/x^3')
legend()
show()
