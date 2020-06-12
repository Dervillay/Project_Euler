# Get length of longest repeating decimal sequence of 1/d
def longest_decimal_seq(d):
    x = 9
    r = x
    length = 1
    while r % d and length < 1000:
        r = r * 10 + x
        length += 1

    # Handle infinite loops on non-repeating decimals by returning 1
    if length < 1000:
        return length
    else:
        return 1

longest = 1
res = 0
for i in range(1, 1000):
    seq_len = longest_decimal_seq(i)

    if seq_len > longest:
        longest = seq_len
        res = i

print(res)