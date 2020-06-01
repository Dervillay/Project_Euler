# Lengths of units as words
unit_lens = {1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4}

# Lengths of 10-19 as words
teen_lens = {10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8}

# Lengths of 10s as words (excluding 10)
tens_lens = {10: 3, 20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6}

# Gives length as word for any number in range 1 to 9999
def len_as_word(n):
    length = 0
    num_len = len(str(n))

    unit = n % 10

    # Handle one digit numbers
    if num_len == 1:
        return unit_lens[unit]

    tens = (n % 100) - unit

    # Handle last two digits
    if tens == 0 and unit != 0:
        length += unit_lens[unit]

    elif tens == 10 and unit != 0:
        length += teen_lens[tens + unit]

    elif tens >= 10:
        if unit != 0:
            length += unit_lens[unit]
        length += tens_lens[tens]

    # If a two digit number then return
    if num_len == 2:
        return length

    # If n doesn't end in 00, then add 3 to accommodate for the word 'and'
    if tens + unit != 0:
        length += 3

    # Handle last three digits
    hundreds = (n % 1000) - tens - unit

    if hundreds != 0:
        length += unit_lens[hundreds // 100] + 7

    # If a three digit number then return
    if num_len == 3:
        return length

    # Handle last four digits
    thousands = n - hundreds - tens - unit
    length += unit_lens[thousands // 1000] + 8

    return length


sum = 0

for i in range(1, 1001):
    sum += len_as_word(i)

print(sum)

