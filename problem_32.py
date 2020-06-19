total = 0
products = []

# Takes string of digits and returns whether 1 through 9 pandigital
def is_pandigital(n):
    set_n = {x for x in n}
    digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

    if set_n == digits and len(n) == 9:
        return True
    else:
        return False

# Length of multiplier i, multiplicand j and product p sum to 9 iff len(m) + len(n) = 5
# Therefore, we can find all pandigital nums using i < 100, j < 10000 / (i+1) by brute force
for i in range(1, 100):
    for j in range(i+1, 10000//(i+1)):
        product = i * j

        full_num = "".join([str(i), str(j), str(product)])

        if is_pandigital(full_num):
            products.append(product)

print(sum(set(products)))