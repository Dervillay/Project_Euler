collatz_lens = {}

# Find Collatz sequence length for n and add to memoized dictionary
def collatz_len(n):

    # Check if n already in memoized dictionary
    if n in collatz_lens:
        return

    seq = [n]

    m = n

    while m != 1:
        if m % 2 == 0:
            m //= 2
        else:
            m = 3*m + 1

        # Check if m already in memoized dictionary
        if m in collatz_lens:
            # Add original n to dictionary
            seq_len = len(seq) + collatz_lens[m]
            collatz_lens[n] = seq_len
            return

        seq.append(m)

    collatz_lens[n] = len(seq)
    return

for i in range(1, 1000000):
    collatz_len(i)

print(max(collatz_lens, key=collatz_lens.get))
