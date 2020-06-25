from math import floor
import numpy as np

A = np.array([[1, -2, 2],
             [2, -1, 2],
             [2, -2, 3]])

B = np.array([[1, 2, 2],
             [2, 1, 2],
             [2, 2, 3]])

C = np.array([[-1, 2, 2],
             [-2, 1, 2],
             [-2, 2, 3]])

# Generate first [3^(d+1)-1]/2 primitive pythagorean triples
# i.e. generates ternary tree of depth d
def primitive_pythag_triples(d):
    max_size = floor(3**(d+1)-1)/2
    triples = []
    triples_at_current_d = [[3, 4, 5]]

    while len(triples) < max_size:
        for triple in triples_at_current_d:
            triples_at_d_plus_one = []

            triples_at_d_plus_one.append(np.matmul(A, triple).tolist())
            triples_at_d_plus_one.append(np.matmul(B, triple).tolist())
            triples_at_d_plus_one.append(np.matmul(C, triple).tolist())

        triples.extend(triples_at_current_d)
        triples_at_current_d = triples_at_d_plus_one

    return triples

# Naive function to return divisors of n
def divisors(n):
    divs = []

    for i in range(1, n//2 + 1):
        if n % i == 0:
            divs.append(i)

    return divs

triple_sums = {}

# Only use triples from pythag triple tree up to a depth of 3 since
# all triples of depth > 3 sum to more than 1000
for triple in primitive_pythag_triples(3):

    triple_sum = sum(triple)

    if triple_sum < 1000:
        if triple_sum in triple_sums:
            triple_sums[triple_sum] += 1
        else:
            triple_sums[triple_sum] = 1

# Find all divisors of a number then sum number of primitive triples that sum to each divisor
largest_no_triples = 0
num_with_largest_no_triples = 0

for num in triple_sums:
    new_no_triples = triple_sums[num]
    divs = divisors(num)

    for d in divs:
        if d in triple_sums:
            new_no_triples += triple_sums[d]

    if new_no_triples > largest_no_triples:
        largest_no_triples = new_no_triples
        num_with_largest_no_triples = num

print(num_with_largest_no_triples)