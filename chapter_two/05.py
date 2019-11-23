from pylab import exp, sqrt, pi, plot, show, linspace


def normal(x, mu, sigma):
    return exp(-(x - mu) ** 2 / 2 * sigma ** 2) / sqrt(2 * pi * sigma ** 2)


x = linspace(-5, 5, 1000)
plot(x, normal(x, 0, 1))
show()

plot(x, normal(x, 0, 5))
plot(x, normal(x, 0, .5))
show()

plot(x, normal(x, 0, 1))
plot(x, normal(x, 1, 1))
plot(x, normal(x, 2, 1))
show()