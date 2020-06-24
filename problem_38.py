# Takes string of digits and returns whether 1 through 9 pandigital
def is_pandigital(n):
    set_n = {x for x in n}
    digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

    if set_n == digits and len(n) == 9:
        return True
    else:
        return False

largest_pandigital = 0

# Since n > 1, for the largest possible i that could produce a pandigital concatenation,
# the number produced will be will be (1 * i) concatenated with (2 * i), which must be 9
# digits long. Therefore there is no need to try values of i with more than 4 digits
for i in range(1, 10000):
    str_total = ""
    n = 1
    while len(str_total) < 9:
        str_total += str(n*i)
        n += 1

    if is_pandigital(str_total) and int(str_total) > largest_pandigital:
        largest_pandigital = int(str_total)

print(largest_pandigital)