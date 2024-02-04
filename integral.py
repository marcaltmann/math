from sympy import symbols, integrate

x = symbols('x')
f = x**2 + 1

area = integrate(f, (x, 0, 1))
print(area)
