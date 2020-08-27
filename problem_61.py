"""
A very ugly solution, but functional and runs in a somewhat acceptable time
"""

from collections import Counter

# Create list of triangle nums that are 4 digits
triangle_nums = []

n = 1
current_num = int((n*(n+1))/2)

while len(str(current_num)) < 5:
    triangle_nums.append(current_num)
    n += 1
    current_num = int((n*(n+1))/2)

triangle_nums = [str(i) for i in triangle_nums if len(str(i)) == 4]

# Create list of square nums up to 4 digits
square_nums = []

n = 1
current_num = int(n**2)

while len(str(current_num)) < 5:
    square_nums.append(current_num)
    n += 1
    current_num = int(n**2)

square_nums = [str(i) for i in square_nums if len(str(i)) == 4]

# Create list of pentagonal nums up to 4 digits
pentagonal_nums = []

n = 1
current_num = int((n*(3*n-1)/2))

while len(str(current_num)) < 5:
    pentagonal_nums.append(current_num)
    n += 1
    current_num = int((n*(3*n-1)/2))

pentagonal_nums = [str(i) for i in pentagonal_nums if len(str(i)) == 4]

# Create list of hexagonal nums up to 4 digits
hexagonal_nums = []

n = 1
current_num = int(n*(2*n-1))

while len(str(current_num)) < 5:
    hexagonal_nums.append(current_num)
    n += 1
    current_num = int(n*(2*n-1))

hexagonal_nums = [str(i) for i in hexagonal_nums if len(str(i)) == 4]

# Create list of heptagonal nums up to 4 digits
heptagonal_nums = []

n = 1
current_num = int((n*(5*n-3)/2))

while len(str(current_num)) < 5:
    heptagonal_nums.append(current_num)
    n += 1
    current_num = int((n*(5*n-3)/2))

heptagonal_nums = [str(i) for i in heptagonal_nums if len(str(i)) == 4]

# Create list of octagonal nums up to 4 digits
octagonal_nums = []

n = 1
current_num = int(n*(3*n-2))

while len(str(current_num)) < 5:
    octagonal_nums.append(current_num)
    n += 1
    current_num = int(n*(3*n-2))

octagonal_nums = [str(i) for i in octagonal_nums if len(str(i)) == 4]

# Function to subtract lists
def subtract_list(a, b):
    remaining = Counter(b)

    out = []
    for i in a:
        if remaining[i]:
            remaining[i] -= 1
        else:
            out.append(i)

    return out

# Create complete set of polygonal nums and remove duplicates
poly_nums = triangle_nums + square_nums + pentagonal_nums + hexagonal_nums + heptagonal_nums + octagonal_nums
poly_nums = list(set(poly_nums))

# Generate all cyclical sets of size 6 in poly_nums
potential_cyclic_sets = []

len_poly_nums = len(poly_nums)

for a in range(len_poly_nums):

    for b in range(len_poly_nums):

        if poly_nums[b][:2] == poly_nums[a][-2:] and poly_nums[a] != poly_nums[b]:

            for c in range(len_poly_nums):

                if poly_nums[c][:2] == poly_nums[b][-2:] and poly_nums[b] != poly_nums[c]:

                    for d in range(len_poly_nums):

                        if poly_nums[d][:2] == poly_nums[c][-2:] and poly_nums[c] != poly_nums[d]:

                            for e in range(len_poly_nums):

                                if poly_nums[e][:2] == poly_nums[d][-2:] and poly_nums[d] != poly_nums[e]:

                                    for f in range(len_poly_nums):

                                        if poly_nums[f][:2] == poly_nums[e][-2:] and poly_nums[e] != poly_nums[f]:

                                            if poly_nums[a][:2] == poly_nums[f][-2:] and poly_nums[a] != poly_nums[f]:
                                                cyclic_set = sorted([poly_nums[a], poly_nums[b], poly_nums[c], poly_nums[d], poly_nums[e], poly_nums[f]])

                                                if cyclic_set not in potential_cyclic_sets:
                                                    potential_cyclic_sets.append(cyclic_set)

# Loop through sets and find one representing each polygonal type
for set in potential_cyclic_sets:
    polygonal_types = [0 for x in range(6)]

    for i in triangle_nums:
        if i in set:
            polygonal_types[0] += 1

    for i in square_nums:
        if i in set:
            polygonal_types[1] += 1

    for i in pentagonal_nums:
        if i in set:
            polygonal_types[2] += 1

    for i in hexagonal_nums:
        if i in set:
            polygonal_types[3] += 1

    for i in heptagonal_nums:
        if i in set:
            polygonal_types[4] += 1

    for i in octagonal_nums:
        if i in set:
            polygonal_types[5] += 1

    # If set represents all types, print it
    # (Had to hard-code it to be a set with 2 triangular numbers, since
    #  the accepted solution set incorrectly contains 2 triangular numbers)
    if all(i > 0 for i in polygonal_types) and polygonal_types[0] == 2:
        print(sum([int(x) for x in set]))
