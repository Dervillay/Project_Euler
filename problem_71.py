# Find greatest common divisor of a and b using Euclid's algorithm
def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

# Generate proper fraction closest to 3/7 for each
# n <= 1,000,000 and return largest amongst these
closest = [1, 1000000]
for n in range(1, 1000001):

    # Calculate fraction closest to but less than 3/7
    frac = [int((3/7) * n), n]

    # Skip over 3/7 and improper fractions
    if frac[0]/frac[1] == 3/7 or gcd(frac[1], frac[0]) != 1:
        continue

    # Check if fraction's value is greater than closest found yet,
    # if so, replace closest
    if frac[0]/frac[1] > closest[0]/closest[1]:
        closest = frac

print(closest[0])