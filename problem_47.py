from math import sqrt

def distinct_prime_factors(n):
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

    return list(set(factors))

i = 647

# Iterate over increasing integers until target found
while True:
    if len(distinct_prime_factors(i)) == 4:

        if len(distinct_prime_factors(i+1)) == 4:

            if len(distinct_prime_factors(i+2)) == 4:

                if len(distinct_prime_factors(i+3)) == 4:

                    print(i)
                    break

                i += 4
                continue

            i += 3
            continue

        i += 2
        continue

    i += 1