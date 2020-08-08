from math import sqrt
from itertools import combinations

def is_prime(n):
    if n < 3:
        return n == 2

    elif n % 2 == 0:
        return False

    for i in range(3, int(sqrt(n))+1, 2):
        if n % i == 0:
            return False

    return True

# Sieve of Eratosthenes to generate list of primes
def list_primes(upto):
    nums = list(range(2, upto+1))

    prime = 2

    while prime <= int(sqrt(upto)):

        for i in range(2*(prime-1), upto-1, prime):
            nums[i] = 0

        prime += 1

    nums = list(filter(lambda x: x != 0, nums))

    return nums

# Returns integer concatenation of integers a and b
def concat(a, b):
    return int(str(a) + str(b))


# Takes a list and returns whether all elements are primes
def all_prime(nums):
    for num in nums:
        if not is_prime(num):
            return False

    return True

# Exclude 2 since this cannot belong to target set of primes
primes_to_calc = 10000
primes = list_primes(primes_to_calc)[1:]
len_primes = len(primes)

smallest_sum = 5 * primes[-1]

# Create hash map, where index i stores all numbers greater than i
# that concatenate with it to make primes
hash_map = [[] for i in range(primes_to_calc)]

# Populates hash map index n with all primes > n that concatenate with n to form primes
def populate_pairs(n):
    for i in range(n + 1, len_primes):
        if is_prime(concat(primes[n], primes[i])) and is_prime(concat(primes[i], primes[n])):
            hash_map[n].append(primes[i])

# Calculate smallest sum using brute force
for i in range(1, len_primes):
    if primes[i] * 5 >= smallest_sum:
        break
    if not hash_map[i]:
        populate_pairs(i)

    for j in range(i+1, len_primes):
        if primes[i] + primes[j] * 4 >= smallest_sum:
            break
        if primes[j] not in hash_map[i]:
            continue
        if not hash_map[j]:
            populate_pairs(j)

        for k in range(j+1, len_primes):
            if primes[i] + primes[j] + primes[k] * 3 >= smallest_sum:
                break
            if primes[k] not in hash_map[i] or primes[k] not in hash_map[j]:
                continue
            if not hash_map[k]:
                populate_pairs(k)

            for l in range(k+1, len_primes):
                if primes[i] + primes[j] + primes[k] + primes[l] * 2 >= smallest_sum:
                    break
                if primes[l] not in hash_map[i] or primes[l] not in hash_map[j] or primes[l] not in hash_map[k]:
                    continue
                if not hash_map[l]:
                    populate_pairs(l)

                for m in range(l+1, len_primes):
                    if primes[i] + primes[j] + primes[k] + primes[l] + primes[m] >= smallest_sum:
                        break
                    if primes[m] not in hash_map[i] or primes[m] not in hash_map[j] or primes[m] not in hash_map[k] or primes[m] not in hash_map[l]:
                        continue
                    if primes[i] + primes[j] + primes[k] + primes[l] + primes[m] < smallest_sum:
                        smallest_sum = primes[i] + primes[j] + primes[k] + primes[l] + primes[m]
                    break

print(smallest_sum)