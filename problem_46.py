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

# Generate list of primes and two times each square number
prime_nums = primes(10000)
twice_squares = [2*(x**2) for x in range(1, 100)]

target_num = None
curr_num = 9

while not target_num:
    sum_found = False

    # Only consider composite numbers
    if curr_num not in prime_nums:

        for i in prime_nums:

            if i < curr_num:

                for j in twice_squares:

                    if i + j == curr_num:
                        sum_found = True
                        break

                    elif i + j > curr_num:
                        break
            else:
                break

        if not sum_found:
            target_num = curr_num

    curr_num += 2

print(target_num)