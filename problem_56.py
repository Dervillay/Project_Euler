greatest_digit_sum = 0

for a in range(1, 100):
    for b in range(1, 100):
        str_num = str(a**b)
        digit_sum = 0

        for digit in str_num:
            digit_sum += int(digit)

        if digit_sum > greatest_digit_sum:
            greatest_digit_sum = digit_sum

print(greatest_digit_sum)