from pylab import plot, legend, xlabel, sin, show


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
a_t = [acceleration(v_t[0], x_t[0], k, C)]
for i in range(n):
  t.append(t[i] + t_delta)
  v_t.append(v_t[i] + a_t[i] * t_delta)
  x_t.append(x_t[i] + v_t[i] * t_delta)
  a_t.append(acceleration(v_t[i + 1], x_t[i + 1], k, C))

plot(t, x_t, label="x(t)")
plot(t, v_t, label="v(t)")
plot(t, a_t, label="a(t)")
xlabel("t")
legend()


show()


def update_acceleration(v, x, k, C):
  return -k * sin(x) - C * v


def euler_method_acceleration(n):
  t_delta = .01
  C = 5
  k = 10
  x_i = 0
  v_i = 1
  t_i = 0
  a_i = acceleration(v_i, x_i, k, C)
  num = 0
  while num < n + 1:
    yield t_i, v_i, x_i, a_i
    t_i = t_i + t_delta
    x_i = x_i + v_i * t_delta
    v_i = v_i + a_i * t_delta
    a_i = acceleration(v_i, x_i, k, C)
    num += 1


euler = list(euler_method_acceleration(100))

for i in range(n):
  assert euler[i][0] == t[i]
  assert euler[i][1] == v_t[i]
  assert euler[i][2] == x_t[i]
  assert euler[i][3] == a_t[i]
