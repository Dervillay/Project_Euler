
# Calculate generalised pentagonal number according to https://en.wikipedia.org/wiki/Pentagonal_number
def generalised_pentagonal_number(summand_index):
    if summand_index % 2 == 0:
        n = summand_index//2 + 1
    else:
        n = -(summand_index//2 + 1)
    return n * (3*n - 1) / 2 


# Function calculting number of integer partitions (from https://en.wikipedia.org/wiki/Pentagonal_number_theorem)
def num_partitions(n):
    partitions[n] = 0
    summand_index = 0
    pentagonal_num = 1

    while pentagonal_num <= n:
        sign = -1 if summand_index % 4 > 1 else 1
        partitions[n] += sign * partitions[n - pentagonal_num]
        summand_index += 1

        pentagonal_num = generalised_pentagonal_number(summand_index)
    
    return partitions[n]

partitions = {0: 1}

n = 1

while num_partitions(n) % 1000000 != 0:
    n += 1

print(n)
    