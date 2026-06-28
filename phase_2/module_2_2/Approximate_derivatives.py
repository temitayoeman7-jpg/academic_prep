import matplotlib.pyplot as plt

def f(x):
  return x**2
def derivative(f,x,h=0.0001):
  return((f(x+h) - f(x)) / h)
numbers=range(1,6)
for x in numbers:
  print(derivative(f,x))
def g(x):
  return 2 *x
x_values=list(range(-5,6))
y_values=[g(x) for x in x_values]
y_values_2=[derivative(f,x) for x in x_values]

plt.plot(x_values,y_values,label="2x")
plt.plot(x_values,y_values_2,label="numerical derivative")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()