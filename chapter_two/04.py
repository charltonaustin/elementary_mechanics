# coding=utf-8
from pylab import cos, pi, sin


def unit_vector_radians(radians):
    return cos(radians), sin(radians)


def print_out(numerator, denominator):
    assert denominator != 0
    value = (numerator / denominator) * pi
    if numerator == 0:
        print("unit vector for {} angle is {}".format(numerator, unit_vector_radians(value)))
    elif numerator == 1:
        print("unit vector for π/{} angle is {}".format(denominator, unit_vector_radians(value)))
    elif (numerator % denominator) == 0:
        print("unit vector for {}π angle is {}".format(numerator / denominator, unit_vector_radians(value)))
    else:
        print("unit vector for {}π/{} angle is {}"
              .format(numerator, denominator, unit_vector_radians(value)))


print_out(0, 1)
print_out(1, 6)
print_out(1, 3)
print_out(1, 2)
print_out(3, 2)
print_out(4, 2)
print_out(2, 1)


def degrees_to_radians(degrees):
    return degrees * (pi / 180)


def unit_vector_degrees(degrees):
    return cos(degrees_to_radians(degrees)), sin(degrees_to_radians(degrees))
