from pylab import arctan, pi


def theata(x, y):
    return arctan(y / x)


def theata_in_pi(x, y):
    return arctan(y / x) % pi


def print_out(x, y):
    print("angles theata for {},{}".format(x, y))
    print(theata(x, y))
    print("angles theata for {},{} in [0, pi]".format(x, y))
    print(theata_in_pi(x, y))


print_out(1, 1)
print_out(-1, 1)
print_out(-1, -1)
print_out(1, -1)
