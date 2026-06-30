import matplotlib.pyplot as plt

def f(x):
    return x**2

a, b, n = 0, 3, 10
width = (b - a) / n

x_positions = []
heights = []

for i in range(n):
    x = a + i * width
    x_positions.append(x)
    heights.append(f(x))


plt.bar(x_positions, heights, width=width, align='edge', alpha=0.5, edgecolor='black', color='skyblue', label='Rectangles')


steps = int((b - a) / 0.01) 
curve_x = [a + i * 0.01 for i in range(steps)]
curve_y = [f(x) for x in curve_x]
plt.plot(curve_x, curve_y, color='red', linewidth=2, label='f(x) = x²')


plt.title(f'Left Riemann Sum Visualization (n = {n})')
plt.xlabel('Ground Position (x)')
plt.ylabel('Height (y)')
plt.legend()  
plt.grid(True, alpha=0.2)  

plt.show()

