from collections import Counter
from math import ceil, sqrt

# Pre-compute smallest prime factor using O(Log n)
# Sieve of Eratosthenes for each N <= 1,000,000
max = 1000001
spf = [0 for i in range(max)]

def sieve():
    spf[1] = 1

    for i in range(2, max):
        spf[i] = i

    for i in range(4, max, 2):
        spf[i] = 2

    for i in range(3, ceil(sqrt(max))):

        if spf[i] == i:

            for j in range(i**2, max, i):

                if spf[j] == j:
                    spf[j] = i

# Run sieve to precompute smallest prime factors
sieve()

# Return a counter of n's prime factors
# e.g. 100 = 2^2 * 5^2, so
# 100 -> {2: 2, 5: 2}
# (Due to precomputed SPFs this takes O(Log n))
def prime_factors(n):
    factors = []

    while n != 1:
        factors.append(spf[n])
        n //= spf[n]

    return Counter(factors)

# Return the value of phi(n) where phi
# represents Euler's totient function
def totient(n):

    # Decompose n into prime factors
    factors = prime_factors(n)

    # Use the theorem:
    # phi(n) = (p1^k1)*(p2^k2)*...*(pr^kr)*(1 - 1/p1)*(1 - 1/p2)*...*(1 - 1/pr),
    # where each pi^ki is a prime factor of n,
    # to calculate phi(n)
    result = 1
    for p in factors:
        result *= (p**factors[p]) * (1 - 1 / p)

    return int(result)

# Iteratively calculate n/phi(n) for n <= 1,000,000 and find n for which
# n/phi(n) is maximum
largest_val = 0
max_n = 0

for n in range(2, 1000001):
    val = n/totient(n)

    if val > largest_val:
        largest_val = val
        max_n = n

print(max_n)

