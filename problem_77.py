from math import sqrt

# Sieve of Eratosthenes
def list_primes(upto):
    nums = list(range(2, upto+1))
    prime = 2

    while prime <= int(sqrt(upto)):
        for i in range(2*(prime-1), upto-1, prime):
            nums[i] = 0
        prime += 1

    return list(filter(lambda x: x != 0, nums))

# DP coin change algorithm
def count_prime_sums(primes, num_primes, n):

    # Store num of prime sums equal to n when using first m primes
    num_of_prime_sums = [[0 for _ in range(num_primes)] for _ in range(n+1)]

    for i in range(num_primes):
        num_of_prime_sums[0][i] = 1

    for i in range(1, n+1):
        for j in range(num_primes):
            x = num_of_prime_sums[i - primes[j]][j] if i-primes[j] >= 0 else 0
            y = num_of_prime_sums[i][j-1] if j >= 1 else 0

            num_of_prime_sums[i][j] = x + y

    return num_of_prime_sums[n][num_primes-1]

prime_nums = list_primes(5000)
n = 2

while True:
    if count_prime_sums(prime_nums, len(prime_nums), n) > 5000:
        print(n)
        break
    n += 1
    