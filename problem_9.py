def pythag_triples(lim):
    triples = []
    n = 1
    m = 1

    for i in range(lim):
        for j in range(lim):
            triple = []
            triple.append(4*m*n - 2*n + 4*(m**2) - 4*m + 1)
            triple.append(2*(n**2) + 4*m*n - 2*n)
            triple.append(2*(n**2) + 4*m*n - 2*n + 4*(m**2) - 4*m + 1)
            triples.append(triple)
            n += 1
        n = 1
        m += 1

    return triples

triples = pythag_triples(10)

# Find the triple that sums to 1000
for i in triples:
    if i[0] + i[1] + i[2] == 1000:
        triple = i

print(triple[0]*triple[1]*triple[2])