from sympy import symbols, limit, oo

x = symbols('x')
f = 1 / x
result = limit(f, x, oo)

n = symbols('n')
f2 = (1 + (1/n))**n
result2 = limit(f2, n, oo)

print(result)
print(result2)
print(result2.evalf())
