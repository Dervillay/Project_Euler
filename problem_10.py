from math import sqrt

# Sieve of Eratosthenes
nums = list(range(2, 2000000))

prime = 2

while prime <= int(sqrt(2000000)):

    for i in range(2*(prime-1), 1999998, prime):
        nums[i] = 0

    prime += 1

nums = list(filter(lambda x: x != 0, nums))

print(sum(nums))
