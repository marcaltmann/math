from sympy import symbols, diff

x, y = symbols('x y')

# Ableitung für erste Funktion muss mit Unterstrich versehen werden,
# um Variablenkonflikte zu vermeiden.
_y = x**2 + 1
dy_dx = diff(_y)

# Ableitung für zweite Funktion
z = y**3 - 2
dz_dy = diff(z)

# Ableitung berechnen mit und ohne Kettenregel,
# Funktion y substituieren.
dz_dx_chain = (dy_dx * dz_dy).subs(y, _y)
dz_dx_no_chain = diff(z.subs(y, _y))

# Kettenregel beweisen, zeigen, dass beide gleich sind.
print(dz_dx_chain)
print(dz_dx_no_chain)
