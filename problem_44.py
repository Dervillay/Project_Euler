from math import sqrt

# Create ordered list of pentagonal nums
def pentagonal_nums_up_to(n):
    nums = []

    for i in range(1, n+1):
        nums.append(int(i*((3*i-1)/2)))

    return nums

# Applies the quadratic formula to the rearranged Pentagonal number formula:
# 3n^2 - n - 2Pn = 0
# Where n is the index of the Pentagonal number and Pn is the number itself.
# We only return one solution since the other is negative for all pentagonal nums
# If the solution is an integer, the supplied number is pentagonal
def get_n_from_pent_num(pentagonal_num):
    return (1+sqrt(1+24*pentagonal_num))/6

pentagonal_nums = pentagonal_nums_up_to(10000)
smallest = None

for i in range(len(pentagonal_nums)-1):
    for j in range(i+1, len(pentagonal_nums)):

        pentagonal_sum = pentagonal_nums[i] + pentagonal_nums[j]
        if get_n_from_pent_num(pentagonal_sum).is_integer():

            pentagonal_diff = pentagonal_nums[j] - pentagonal_nums[i]
            if get_n_from_pent_num(pentagonal_diff).is_integer():

                val = abs(pentagonal_diff)

                if not smallest or val < smallest:
                    smallest = val

print(smallest)
