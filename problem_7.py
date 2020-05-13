from math import sqrt

# Sieve of Eratosthenes
def primes(upto):
    nums = list(range(2, upto+1))

    prime = 2

    while prime <= int(sqrt(upto)):

        for i in range(2*(prime-1), upto-1, prime):
            nums[i] = 0

        prime += 1

    nums = list(filter(lambda x: x != 0, nums))

    return nums

print(primes(1000000)[10000])
