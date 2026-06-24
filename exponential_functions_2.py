import matplotlib.pyplot as plt
import math
def v(t):
    return math.exp(-t/0.5)
def g(t):
    return math.exp(-t/2)
def f(t):
    return math.exp(-t/10)
x_values=list(range(0,21))
small=[v(t) for t in x_values]
medium=[g(t) for t in x_values]
large=[f(t) for t in x_values]
plt.plot(x_values,small,label="e^(-t/0.5)")
plt.plot(x_values,medium,label="V(t) = e^(-t/2)")
plt.plot(x_values,large,label="V(t) = e^(-t/10)")
plt.xlabel("x")
plt.ylabel("v(t)")
plt.grid(True)
plt.legend()
plt.show()