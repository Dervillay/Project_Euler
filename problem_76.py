# We answer this question by calculating integer partitions
# using the recurrence relation specified here:
# https://en.wikipedia.org/wiki/Partition_function_(number_theory)

# Return the nth pentagonal number
def pentagonal(n):
    return int(n*(3*n-1) / 2)

# Initialise dict of partitions s.t. partitions[i] is the no. of partitions
# for integer i (we assume 0 is 1)
partitions = {0: 1}

# Returns number of ways to partition an integer n
def calc_partitions(n):
    p = 1
    i = 0
    pentagonal_num = pentagonal(p)
    num_partitions = 0

    # Create list to determine when to add or subtract terms
    add_term = []
    for j in range(0, n, 4):
        add_term.extend([True, True, False, False])
    
    # Calculate recurrence relation
    while n - pentagonal_num >= 0:

        # Determine whether to add or subtract current term
        if add_term[i]:
            num_partitions += partitions[n-pentagonal_num]
        else:
            num_partitions -= partitions[n-pentagonal_num]

        # Alternate between postive and negative i values
        p *= -1
        if p > 0:
            p += 1

        # Increment the index and calculate next pentagonal num
        i += 1
        pentagonal_num = pentagonal(p)

    return num_partitions

# Calculate all partition lengths up to 100 (since recurrence relationship requires
# previous integers' partitions to be known)
for i in range(1, 101):
    partition = calc_partitions(i)
    partitions[i] = partition

# Print number of partitions for 100 (excluding the partition 100 itself)
print(partitions[100] - 1)




