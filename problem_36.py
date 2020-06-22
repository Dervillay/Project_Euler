def to_binary(n):
    return bin(n)[2:]

total = 0

for i in range(1000000):
    str_i = str(i)
    if str_i == str_i[::-1]:
        bin_i = to_binary(i)
        if bin_i == bin_i[::-1]:
            total += i

print(total)