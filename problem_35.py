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

def list_rotations(n):
    str_n = str(n)
    len_n = len(str_n)
    rotations = []

    for i in range(len_n-1):
        str_n = str_n[1:] + str_n[0]
        rotations.append(int(str_n))

    return rotations


# Initialise total with the 13 circular primes under 100
total = 13

for i in range(101, 1000000, 2):
    circular_prime = False
    rotations = []

    if is_prime(i):
        rotations = list_rotations(i)
        circular_prime = True
        for r in rotations:
            if not is_prime(r):
                circular_prime = False
                break

    if circular_prime:
        total += 1

print(total)



