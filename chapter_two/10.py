from random import randint

from pylab import zeros


def roll_dice():
  return randint(1, 6)


def n_rolls(n):
  z = zeros(n)
  for i in range(n):
    z[i] = roll_dice() + roll_dice()
  return z


def average(z):
  return (1 / len(z)) * sum(z)


def standard_deviation(z):
  return (1 / (len(z) - 1)) * (sum(z) - average(z)) ** 2


rolls = n_rolls(100)
print("the average of {} dice rolls is {}".format(100, average(rolls)))
print("the standard deviation of {} dice rolls is {}".format(100, standard_deviation(rolls)))
