from fractions import Fraction

root_two_expansions = {1: Fraction(1 + 1/2)}

# Memoization approach that populates the root_two_expansions dictionary with the value
# of the ith expansion for 1 <= i <= 1000
def populate_root_two_expansions(iterations):
    for i in range(2, iterations + 1):
        root_two_expansions[i] = Fraction(1 + 1/(1 + root_two_expansions[i-1]))

populate_root_two_expansions(1000)
total = 0

# Count number of expansions where numerator has more digits than denominator
for fraction in root_two_expansions.values():
    if len(str(fraction.numerator)) > len(str(fraction.denominator)):
        total += 1

print(total)