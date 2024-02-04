from sympy import symbols, plot, log, ln

x = symbols('x')

f1 = ln(x)
f2 = log(x, 2)
f3 = log(x, 3)
f4 = log(x, 10)
plot(f1, f2, f3, f4)
