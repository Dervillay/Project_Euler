total = 0

for i in range(2, 1000000):
    str_i = str(i)
    sum_of_powers = sum([int(x)**5 for x in str_i])
    if sum_of_powers == i:
        total += i

print(total)