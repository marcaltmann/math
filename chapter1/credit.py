from math import exp, e

p = 100
r = .20
t = 2.0
#n = 525600

#a = p * (1 + (r/n))**(n * t)

a = p * exp(r * t)

print(a)
print(e)
