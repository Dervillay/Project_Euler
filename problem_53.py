from math import factorial

def n_choose_r(n, r):
    return factorial(n) / (factorial(r) * factorial(n-r))

total = 0

for n in range(23, 101):
    for r in range(1, n):
        if n_choose_r(n, r) > 1000000:
            total += 1

print(total)
