def riemann_sum(f,a,b,n):
  width_of_rectangle=(b-a)/n
  total=0
  for i in range(n):
    x=a + i * width_of_rectangle
    height=f(x)
    total=total+(width_of_rectangle* height)
  return total

def f(x):
    return x**2

print(riemann_sum(f, 0, 3, 3))
print(riemann_sum(f, 0, 3, 100))
print(riemann_sum(f, 0, 3, 10000))