from math import sqrt
from itertools import permutations

def is_prime(n):
    if n < 3:
        return n == 2

    elif n % 2 == 0:
        return False

    for i in range(3, int(sqrt(n))+1, 2):
        if n % i == 0:
            return False

    return True

largest_pandigital_prime = 0

# Generate all pandigital numbers for 1 to i for decreasing i and check whether prime
# then return the largest found
for i in range(10, 0, -1):
    pandigital_primes = [int(''.join(p)) for p in permutations([str(x) for x in range(1, i)]) if is_prime(int(''.join(p)))]

    if pandigital_primes:
        largest_pandigital_prime = max(pandigital_primes)
        break

print(largest_pandigital_prime)
