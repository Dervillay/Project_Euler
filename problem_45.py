from math import sqrt

# Create ordered list of hexagonal nums from H144 onwards
def hexagonal_nums_up_to(n):
    nums = []

    for i in range(144, n+1):
        nums.append(int(i*(2*i-1)))

    return nums

# Applies the quadratic formula to the rearranged Triangle number formula:
# n^2 + n - 2Tn = 0
# If the solution is an integer, the supplied number is triangular
def n_from_tri_num(triangle_num):
    return (-1+sqrt(1+8*triangle_num))/2

# Applies the quadratic formula to the rearranged Pentagonal number formula:
# 3n^2 - n - 2Pn = 0
# If the solution is an integer, the supplied number is pentagonal
def n_from_pent_num(pentagonal_num):
    return (1+sqrt(1+24*pentagonal_num))/6

# Applies the quadratic formula to the rearranged Triangle number formula:
# 2n^2 - n - Hn = 0
# If the solution is an integer, the supplied number is hexagonal
def n_from_hex_num(hexagonal_num):
    return (1+sqrt(1+8*hexagonal_num))/4

hexagonal_nums = hexagonal_nums_up_to(100000)

for num in hexagonal_nums:
    triangle_n = n_from_tri_num(num)
    pentagonal_n = n_from_pent_num(num)

    if triangle_n.is_integer() and pentagonal_n.is_integer():
        print(num)
        exit()



