from sympy import symbols, diff

x = symbols('x')
f = x**2

dx_f = diff(f)
print(dx_f)
