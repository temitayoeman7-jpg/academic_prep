import math
import matplotlib.pyplot as plt
def y(f):
  return math.exp(f)
def g(f):
  return math.log(f)
def h(f):
  return math.sin(f)
def evaluate(f,x_values):
  y_values=[f(x) for x in x_values]
  return y_values
x_values = [x * 0.1 for x in range(1, 51)]
exp_values = evaluate(y, x_values)
plt.plot(x_values, exp_values, label="e^x")
log_values = evaluate(g, x_values)
plt.plot(x_values, log_values, label="ln(x)")
sin_values = evaluate(h, x_values)
plt.plot(x_values, sin_values, label="sin(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()