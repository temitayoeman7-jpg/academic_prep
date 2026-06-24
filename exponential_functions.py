import matplotlib.pyplot as plt
import math
def f(x):
    return math.exp(x)
def g(x):
    return math.exp(-x)

x_values=list(range(-5,6))
y_values=[f(x) for x in x_values]
y_2values=[g(x) for x in x_values]
plt.plot(x_values,y_values,label="f(x) = e^x")
plt.plot(x_values,y_2values, label="g(x) = e^(-x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()