from fractions import Fraction

# Using a modified version of the algorithm given here:
# https://en.wikipedia.org/wiki/Farey_sequence

# Generate Farey sequence F_n
# starting at 1/3 and ending at 1/2
def farey_sequence(n):
    # Calculate fraction appearing before 1/3,
    # since algorithm requires two consecutive fractions
    # in order to calculate the next fraction
    prev_frac = Fraction(int(n/3 - 1), n)
    a, b = prev_frac.numerator, prev_frac.denominator
    c, d = 1, 3

    seq = []

    while a != 1 or b != 2:
        k = (n + b) // d
        a, b, c, d = c, d, k * c - a, k * d - b
        seq.append([a, b])

    return seq

# Print length of generated sequence minus the terms 1/3 and 1/2
seq = farey_sequence(12000)
print(len(seq) - 2)