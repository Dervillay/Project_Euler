"""
From number theory is is known that if a formula
p(x) = x^2 + x + 41
is prime generating for 0 <= x <= n, then so is p(x-n).
(See https://mathworld.wolfram.com/Prime-GeneratingPolynomial.html)

Since we obtain
n^2 - 79n + 1601
from
(n-40)^2 + (n-40) + 41

We can find other prime-generating formulae of this form by iteratively expanding
(n-i)^2 + (n-i) + 41, for i <= 40
to the form
n^2 + an + b
until we find the first i where we have |a| < 1000 and |b| <= 1000.
"""

# Expands the formula (x-n)^2 + (x-n) + 41 to the form n^2 + an + b
# and returns a and b
def expand_quadratic_formula(n):
    a = (-2*n) + 1
    b = n**2 - n + 41
    return a, b

for i in range(40, -1, -1):
    a, b = expand_quadratic_formula(i)
    if abs(a) < 1000 and abs(b) <= 1000:
        print(a*b)
        exit()
