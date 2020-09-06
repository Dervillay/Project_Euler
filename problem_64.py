"""
Solution using algorithm described here:
https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion
"""

from math import sqrt

# Outputs an integer representing the period length
# of the continued fraction representation of sqrt(n)
def continued_fraction(n):

    limit = int(sqrt(n))
    period_len = 0
    d = 1
    m = 0
    a = limit

    # Iteratively apply the algorithm and count period length
    while a != 2*limit:
        m = d*a - m
        d = (n - m**2) / d
        a = int((limit + m) / d)

        period_len += 1

    return period_len

# Initialise counter
count = 0

# For i from 2 to 10,000, increment count if sqrt(i) is irrational and has an odd period
for i in range(2, 10001):
    if int(sqrt(i)) ** 2 != i and continued_fraction(i) % 2 == 1:
        count += 1

print(count)