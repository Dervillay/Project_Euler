from fractions import Fraction

# Generate list of first 100 terms in representation of continued fraction
continued_fract = [2]
for i in range(1, 34):
    continued_fract.extend([1, 2 * i, 1])

# Outputs a fraction representing the nth convergent of e
def nth_convergent(n):
    integer_part = continued_fract[0]

    # Handle special case for n = 1
    if n == 1:
        return integer_part

    # Handle all other cases
    fract_part = continued_fract[n - 1]
    for i in range(n-2, 0, -1):
        current_val = continued_fract[i]
        fract_part = current_val + Fraction(1 / fract_part)

    return Fraction(integer_part + Fraction(1 / fract_part))

# Find 100th convergent and sum digits of numerator
print(sum(int(digit) for digit in str(nth_convergent(100).numerator)))