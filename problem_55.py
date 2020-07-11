# Determine Lychrel numbers over 50 iterations
def is_lychrel_num(num):
    for i in range(49):
        num += int(str(num)[::-1])

        if str(num) == str(num)[::-1]:
            return False

    return True

total = 0

for num in range(1, 10000):
    if is_lychrel_num(num):
        total += 1

print(total)