from pylab import plot, show, legend


def create_logistics(r):
    def logistic(x_of_i):
        return r * x_of_i * (1 - x_of_i)

    return logistic


x_of_i = .5
ys = []
logistics = []
for i in range(0, 4):
    logistics.append(create_logistics(i + 1))
    ys.append([x_of_i])

for i in range(1, 100):
    for j, logistic in enumerate(logistics):
        ys[j].append(logistic(ys[j][i - 1]))

for i, y in enumerate(ys):
    plot(y, label="r={}".format(i+1))
legend()
show()
