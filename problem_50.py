from math import sqrt

# Sieve of Eratosthenes to generate list of primes
def primes(upto):
    nums = list(range(2, upto+1))

    prime = 2

    while prime <= int(sqrt(upto)):

        for i in range(2*(prime-1), upto-1, prime):
            nums[i] = 0

        prime += 1

    nums = list(filter(lambda x: x != 0, nums))

    return nums

def is_prime(n):
    if n < 3:
        return n == 2

    elif n % 2 == 0:
        return False

    for i in range(3, int(sqrt(n))+1, 2):
        if n % i == 0:
            return False

    return True

prime_nums = primes(1000000)
len_prime_nums = len(prime_nums)

target = 0
most_consecutive_primes = 0

for i in range(0, len_prime_nums - 1):
    for j in range(i+1, len_prime_nums):

        total = sum(prime_nums[i:j+1])
        consecutive_primes = j - i + 1

        # If total exceeds largest prime below one-million then break
        if total > 999983:
            break

        if is_prime(total) and consecutive_primes > most_consecutive_primes:
            most_consecutive_primes = consecutive_primes
            target = total

print(target)
