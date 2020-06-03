from math import factorial

num = factorial(100)

total = sum([int(x) for x in str(num)])

print(total)