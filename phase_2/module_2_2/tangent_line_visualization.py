```notebook-python
import matplotlib.pyplot as plt
def f(x):
  return x**2

def derivative(f, x, h=0.0001):
    return (f(x+h) - f(x)) / h
slope=derivative(f,2)
x_values=[x * 0.1 for x in range(-10, 51)]
y_values=[f(x) for x in x_values]
t_values=[f(2) + slope * (x - 2) for x in x_values]

plt.plot(x_values, y_values, label="Curve: f(x) = x²", color="blue")
plt.plot(x_values, t_values, label="Tangent Line at x=2", color="red")
plt.grid(True)
plt.legend()
plt.show()