import math
import matplotlib.pyplot as plt
def f(x):
    return math.log(x)
def g(x):
    return math.exp(x)

x_values = [x * 0.1 for x in range(1, 51)]
y_values=[f(x) for x in x_values]
y_values_2=[g(x) for x in x_values]

plt.plot(x_values,y_values,label="f(x) = ln(x)")
plt.plot(x_values,y_values_2,label="g(x) = e^x")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()