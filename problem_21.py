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


amicable_nums = []

for i in range(1, 10000):
    a = sum(divisors(i))
    b = sum(divisors(a))

    if b == i and a != i:
        amicable_nums.extend([i, a])

print(sum(set(amicable_nums)))
