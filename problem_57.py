import sys
from fractions import Fraction

sys.setrecursionlimit(1020)

# Could be improved using memoization, but this approach still runs
# in well under a minute, so is acceptable for now
def root_two(iterations, first_iteration):
    if iterations == 1:
        if first_iteration:
            return Fraction(1 + 1/2)
        else:
            return Fraction(2 + 1/2)
    elif first_iteration:
        return Fraction(1 + 1/root_two(iterations - 1, False))
    else:
        return Fraction(2 + 1/root_two(iterations - 1, False))

total = 0

for i in range(1, 1001):
    fraction = root_two(i, True)

    if len(str(fraction.numerator)) > len(str(fraction.denominator)):
        total += 1

print(total)