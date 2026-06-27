import math
import matplotlib.pyplot as plt
def f(x):
  return math.sin(x)
def g(x):
  return math.cos(x)
x_values=[x*0.1 for x in range(0,201)]
y_values=[f(x) for x in x_values]
y_values_2=[g(x) for x in x_values]


plt.plot(x_values,y_values,label="sin(x)")
plt.plot(x_values,y_values_2,label="cos(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()
