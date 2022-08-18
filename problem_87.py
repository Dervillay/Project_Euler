from math import sqrt
from collections import defaultdict

limit = 50000000
prime_squares = []
prime_cubes = []
prime_fourth_powers = []

# Use sieve of Eratosthenes to generate primes
def get_primes(upto):
    nums = list(range(2, upto+1))

    prime = 2

    while prime <= int(sqrt(upto)):

        for i in range(2*(prime-1), upto-1, prime):
            nums[i] = 0

        prime += 1

    nums = list(filter(lambda x: x != 0, nums))

    return nums


# Generate all prime squares, cubes and fourth powers using primes up to sqrt(limit)
primes = get_primes(int(sqrt(limit)))
for p in primes:
    p_2 = p**2
    p_3 = p**3
    p_4 = p**4

    if p_2 < limit:
        prime_squares.append(p_2)
    if p_3 < limit:
        prime_cubes.append(p_3)
    if p_4 < limit:
        prime_fourth_powers.append(p_4)

# Iterate over all unique sums of prime_squares, prime_cubes and prime_fourth_powers less than limit
total = 0
seen_before = defaultdict(lambda: False)
for p_2 in prime_squares:
    for p_3 in prime_cubes:
        for p_4 in prime_fourth_powers:
            sum_ = p_2 + p_3 + p_4
            if sum_ < limit and not seen_before[sum_]:
                total += 1
                seen_before[sum_] = True
print(total)
