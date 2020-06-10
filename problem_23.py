from math import sqrt

# O(sqrt(n)) algorithm for finding divisors
def divisors(n):
    divisors = [1]
    i = 1

    while i <= sqrt(n):

        if n % i == 0:

            if n/i == i:
                divisors.append(i)
            elif i != 1:
                divisors.extend([i, n//i])

        i += 1

    return list(set(divisors))

abundant_nums = []

# Find all abundant_nums from 12 to 28123 exclusive
for i in range(12, 28123):
    if sum(divisors(i)) > i:
        abundant_nums.append(i)

len_abundant_nums = len(abundant_nums)

# Generate list of all possible sums using abundant_nums
abundant_num_sums = []
for i in range(len_abundant_nums):

    for j in range(i, len_abundant_nums):

        # Also accounts for adding each number to itself
        num_sum = abundant_nums[i] + abundant_nums[j]

        # Stop once sums start to pass 28123
        if num_sum > 28123:
            break

        abundant_num_sums.append(abundant_nums[i] + abundant_nums[j])

# Generate list of nums to 28123 and take the set difference from abundant_num_sums
nums = set(range(1, 28124))
target_nums = nums.difference(set(abundant_num_sums))

print(sum(target_nums))
