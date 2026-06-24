import matplotlib.pyplot as plt
def f(x):
    return -3*x +5
def g(x):
    return x*x
def y(x):
    return 1+x
def z(x):
    return 2*x + 10
x_values = list(range(-10, 11))
y_values = [f(x) for x in x_values]
y_2values=[g(x) for x in x_values]
y_3values=[y(x) for x in x_values]
y_4values=[z(x) for x in x_values]

plt.plot(x_values, y_values,label="3*x +5")
plt.plot(x_values,y_2values,label="x*2")
plt.plot(x_values,y_3values,label="x+1")
plt.plot(x_values,y_4values,label="2*x+10")
plt.xlabel("x")
plt.ylabel("fx")
plt.grid(True)
plt.legend()

plt.show()
