from pylab import plot, xlabel, show, subplot, ylabel

t = []
x = []
y = []

f = open("trajectory.dat", "r")
for line in f:
  line = line.strip()
  t_i, x_i, y_i = line.split()
  t.append(float(t_i))
  x.append(float(x_i))
  y.append(float(y_i))

subplot(2, 1, 1)
plot(t, x), xlabel('t'), ylabel('x')
subplot(2, 1, 2)
plot(t, y), xlabel('t'), ylabel('y')
show()

plot(x, y), xlabel('x'), ylabel('y')
show()
