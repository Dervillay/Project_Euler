from math import sqrt

def is_prime(n):
    if n < 3:
        return n == 2

    elif n % 2 == 0:
        return False

    for i in range(3, int(sqrt(n))+1, 2):
        if n % i == 0:
            return False

    return True

truncatable_primes = []

i = 10

while len(truncatable_primes) < 11:

    if is_prime(i):
        truncatable_prime = True
        str_i = str(i)

        for index in range(1, len(str_i)):
            trunc_left = int(str_i[index:])
            trunc_right = int(str_i[:-index])

            if not is_prime(trunc_left) or not is_prime(trunc_right):
                truncatable_prime = False
                break

        if truncatable_prime:
            truncatable_primes.append(i)

    i += 1

print(sum(truncatable_primes))