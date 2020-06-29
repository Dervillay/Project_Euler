from itertools import permutations

# List of all permutations of 0123456789 that don't start with 0
pandigital_num_strings = [''.join(p) for p in permutations("0123456789") if p[0] != '0']

target_num_sum = 0

# Iterate over each permutation and check whether target num
for num in pandigital_num_strings:

    if int(num[1:4]) % 2 == 0 and \
       int(num[2:5]) % 3 == 0 and \
       int(num[3:6]) % 5 == 0 and \
       int(num[4:7]) % 7 == 0 and \
       int(num[5:8]) % 11 == 0 and \
       int(num[6:9]) % 13 == 0 and \
       int(num[7:10]) % 17 == 0:

        target_num_sum += int(num)

print(target_num_sum)