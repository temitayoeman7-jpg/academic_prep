def f(x):
    return x**2

def derivative(f, x, h):
    return (f(x+h) - f(x)) / h

for h in [1, 0.1, 0.01, 0.0001, 1e-8, 1e-15]:
    print(f"h={h}: slope = {derivative(f, 3, h)}")