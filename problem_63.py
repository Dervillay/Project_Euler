# Problem can be rephrased as finding integers x that satisfy:
# 10^(n-1) <= x^n < 10^n
# i.e. that x^n is n digits long

# From this, we know that x < 10 is our upper bound, and since our answers
# must be integers, x <= 9

# We can rearrange the left-hand side to find our lower bound
# 10^(n-1) <= x^n
# n-1 <= n * log_10(x)
# (n-1)/n <= log_10(x)
# 10^((n-1)/n) <= x

# As n increases, 10^((n-1)/n) will tend to 10
# Meaning that at some point our lower bound will surpass our upper bound
# and there will be no more solutions

# Now we only have to iterate over positive values of n until our lower bound surpasses 9
# i.e. finding the solutions of:
# 10^((n-1)/n) <= x <= 9

from math import ceil

lower_bound = 0
count = 0
n = 1

while lower_bound < 10:
    lower_bound = int(ceil(10**((n-1)/n)))
    count += 10 - lower_bound
    n += 1

print(count)

