from pylab import plot, xlabel, show, ylabel, subplot

t = []
v = []

f = open("velocityy.dat", "r")
for line in f:
  line = line.strip()
  t_i, v_i = line.split()
  t.append(float(t_i))
  v.append(float(v_i))

plot(t, v), xlabel('t'), ylabel('y')
show()
y = [0]
for i in range(len(v) - 1):
  y.append(y[i] + v[i] * (t[i] - t[i + 1]))

subplot(2, 1, 1)
plot(t, v), xlabel('t'), ylabel('v')
subplot(2, 1, 2)
plot(t, y), xlabel('t'), ylabel('y')
show()
