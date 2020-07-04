from math import sqrt

def is_prime(n):
    if n < 3:
        return n == 2

    elif n % 2 == 0:
        return False

    for i in range(3, int(sqrt(n))+1, 2):
        if n % i == 0:
            return False

    return True

# Only consider odd 4-digit integers, since even integers won't be prime
for num in range(1489, 10000, 2):
    if is_prime(num):
        num_2 = num + 3330
        num_3 = num_2 + 3330

        if is_prime(num_2) and is_prime(num_3):
            sorted_num = sorted(list(str(num)))
            sorted_num_2 = sorted(list(str(num_2)))
            sorted_num_3 = sorted(list(str(num_3)))

            if sorted_num == sorted_num_2 and sorted_num == sorted_num_3:
                print(str(num) + str(num_2) + str(num_3))
                exit()
