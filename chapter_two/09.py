from pylab import plot, show, legend, xlabel, sin


def acceleration(v, x, k, C):
  return -k * x - C * v


t_delta = .01
C = 5
k = 10
x_0 = 0
v_0 = 1
t_0 = 0
n = 100
x_t = [x_0]
v_t = [v_0]
t = [t_0]
a_t = []
for i in range(n + 1):
  a_t.append(acceleration(v_t[i], x_t[i], k, C))
  v_t.append(v_t[i] + a_t[i] * t_delta)
  x_t.append(x_t[i] + v_t[i] * t_delta)
  t.append(t[i] + t_delta)

a_t.append(acceleration(v_t[n], x_t[n], k, C))
plot(t, x_t, label="x(t)")
plot(t, v_t, label="v(t)")
plot(t, a_t, label="a(t)")
xlabel("t")
legend()

show()


def update_acceleration(v, x, k, C):
  return -k * sin(x) - C * v
