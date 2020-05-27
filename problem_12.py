from math import sqrt

def prime_factors(n):
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n /= 2

    for i in range(3, int(sqrt(n))+1, 2):
        while n % i == 0:
            factors.append(i)
            n /= i

    if n > 2:
        factors.append(n)

    return factors


# Returns number of factors for triangular numbers
def num_factors(n):

    p_factors = prime_factors(n)

    factors = 1

    for i in set(p_factors):
        factors *= p_factors.count(i) + 1

    return factors


num = 1
inc = 2

while num_factors(num) <= 500:
    num += inc
    inc += 1

print(num)