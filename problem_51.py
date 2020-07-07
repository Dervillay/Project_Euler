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

# Function to check if a number has any repeating digits
def list_repeating_nums(n):
    str_n = str(n)
    repeating_nums = []
    for i in str_n:
        if str_n.count(i) > 1 and i not in repeating_nums:
            repeating_nums.append(i)

    return repeating_nums


# Generate primes with 3 digits or more
prime_nums = [x for x in primes(1000000) if len(str(x)) >= 5]

target = None

for prime in prime_nums:
    repeating_nums = list_repeating_nums(prime)

    if repeating_nums:
        str_prime = str(prime)

        for num in repeating_nums:
            family = []
            primes_in_family = 0

            # Replace all occurrences of repeating number with i for 0 <= i <= 9
            for i in range(0, 10):
                new_member = [x if x != num else str(i) for x in str_prime]
                new_member_int = int(''.join(new_member))
                new_member_str = str(new_member_int)

                # Avoid including numbers that have been shortened by replacing the first
                # digit with 0
                if len(new_member_str) == len(str_prime):

                    if is_prime(new_member_int):
                        primes_in_family += 1

                    family.append(new_member_int)

            if primes_in_family == 8:
                print(prime)
                exit()