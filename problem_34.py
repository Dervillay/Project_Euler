from math import factorial

total = 0

# Only need to try up to 7 digit numbers since n * 9! gives a number with fewer
# than n digits for n > 7, therefore no curious numbers of length > 7 can exist
# (in practice, we actually find that no curious number exists of length > 5)
for i in range(3, 10000000):
    factorial_sum = 0
    for digit in str(i):
        factorial_sum += factorial(int(digit))

    if factorial_sum == i:
        total += i

print(total)