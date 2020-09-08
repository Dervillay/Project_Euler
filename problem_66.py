"""
Solution uses the method specified here: https://en.wikipedia.org/wiki/Pell%27s_equation#Solutions
to find solutions to the equation x^2 - Dy^2 = 1 using continued fraction convergents of sqrt(D)
"""
from math import sqrt

# Find sequence of convergents for sqrt(n) to determine the minimal
# solution for the Diophantine equation of the form x^2 - n*y^2 = 1,
# returning the x value
def solve_diophantine(n):
    limit = int(sqrt(n))
    d = 1
    m = 0
    a = limit

    h0 = a
    h1 = 1

    k0 = 1
    k1 = 0

    # Iteratively apply algorithm from problem 64 to find convergents,
    # testing them until solution is found
    while h0*h0 - n*k0*k0 != 1:
        m = d*a - m
        d = (n - m**2) / d
        a = int((limit + m) / d)

        h2 = h1
        h1 = h0

        k2 = k1
        k1 = k0

        h0 = a*h1 + h2
        k0 = a*k1 + k2

    return h1

largest_x = 0
result = 0

# Run on all non-square values i <= 1000 to find largest value of x
for i in range(1, 1001):
    if int(sqrt(i))**2 == i:
        continue

    x = solve_diophantine(i)
    if x > largest_x:
        largest_x = x
        result = i

print(result)

