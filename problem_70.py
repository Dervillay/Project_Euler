"""
A rather slow solution using the same approach as problem 69 for calculating
Euler's totient function
"""

from collections import Counter
from math import ceil, sqrt

# Pre-compute smallest prime factor using O(Log n)
# Sieve of Eratosthenes for each N <= 1,000,000
max = 10000000
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

# Returns whether two integers a and b are permutations of each other
def are_perms(a, b):
    if sorted(str(a)) == sorted(str(b)):
        return True
    else:
        return False

# Calculate phi(n) for 1 < n < 10,000,000 where phi(n) is a perm of n
# and n/phi(n) is a minimum
min_val = None
result = None

for n in range(2, 10000000):
    phi_n = totient(n)
    if are_perms(n, phi_n):
        val = n/phi_n

        if min_val == None or val < min_val:
            min_val = val
            result = n

print(result)