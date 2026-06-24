import matplotlib.pyplot as plt
def f(x):
    return -3*x +5
def g(x):
    return x*x
def y(x):
    return 1+x
def z(x):
    return 2*x +13
x_values = list(range(-10, 11))
y_values = [f(x) for x in x_values]
y_2values=[z(x) for x in x_values]
y_3values=[y(x) for x in x_values]

plt.plot(x_values, y_values,label="numbrs in respect to y")
plt.plot(x_values,y_2values,label="squared numbers")
plt.plot(x_values,y_3values,label="x+1")
plt.xlabel("x")
plt.ylabel("fx")
plt.grid(True)
plt.legend()

plt.show()
