from math import sqrt, gcd

# Generate primitive pythagorean triples that
# sum to less than limit using Euclid's formula
def pythag_triples(limit):
    triples = []

    # Stop once c exceeds limit (i.e. when m = sqrt(limit / 2))
    for m in range(2, int(sqrt(limit / 2))):
        for n in range(1, m):

            # Check M and N are not both odd and are coprime
            if (m % 2 == 0 or n % 2 == 0) and gcd(m, n) == 1:

                # Generate primitive triple
                a = m**2 - n**2
                b = 2*m*n
                c = m**2 + n**2

                triples.append([a, b, c])

    return triples

# Generate primitive triples and initialise dictionary to store their sums
triples = pythag_triples(1500000)
triple_sums = {}

# Iterate through triples and store sums and number
# of appearances in triple_sums dict
for t in triples:
    sum_t = sum(t)

    new_sum_t = sum_t
    while new_sum_t <= 1500000:

        # Add multiple of sum_t to triple sums
        if new_sum_t in triple_sums:
            triple_sums[new_sum_t] += 1
        else:
            triple_sums[new_sum_t] = 1

        new_sum_t += sum_t

counter = 0

# Increment counter for each sum appearing only once in dict
for i in triple_sums:
    if triple_sums[i] == 1:
        counter += 1

print(counter)


