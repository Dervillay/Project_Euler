from math import sqrt

# Determine whether integer n is prime
def is_prime(n):
    if n < 3:
        return n == 2

    elif n % 2 == 0:
        return False

    for i in range(3, int(sqrt(n))+1, 2):
        if n % i == 0:
            return False

    return True

# Initialise variables for 3 x 3 spiral
side_length = 3
num_primes = 3
current_num = 9

while num_primes/(2*side_length - 1) >= 0.1:
    side_length += 2

    # Calculate if new diagonal numbers are prime
    for i in range(4):
        current_num += side_length - 1

        if is_prime(current_num):
            num_primes += 1

print(side_length)


"""
A (very slow) brute force solution to find the answer by manually generating each spiral
(kept it here because it would be sacrilege to delete such good (yet useless) code)
"""
# # Generate n * n anti-clockwise spiral (where n is odd)
# def generate_spiral(n):
#     spiral = [[1]]
#
#     for i in range((n-1) // 2):
#         extend_spiral(spiral)
#
#     return spiral
#
# # Extend a spiral by adding another outer layer
# def extend_spiral(spiral):
#     side_length = len(spiral)
#     new_side_length = side_length + 2
#     current_num = spiral[side_length-1][side_length-1] + 1
#
#     # Add new spaces to spiral
#     for y in range(side_length):
#         spiral[y].insert(0, 0)
#         spiral[y].append(0)
#     spiral.insert(0, [0 for x in range(new_side_length)])
#     spiral.append([0 for x in range(new_side_length)])
#
#     # Add new numbers to outer layer
#     x = new_side_length - 1
#     y = new_side_length - 2
#
#     # Draw new right side of spiral
#     for num in range(new_side_length-1):
#         spiral[y-num][x] = current_num
#         current_num += 1
#
#     y -= side_length
#
#     # Draw new top side of spiral
#     for num in range(1, new_side_length):
#         spiral[y][x-num] = current_num
#         current_num += 1
#
#     x -= new_side_length - 1
#
#     # Draw new left side of spiral
#     for num in range(1, new_side_length):
#         spiral[y+num][x] = current_num
#         current_num += 1
#
#     y += new_side_length - 1
#
#     # Draw new bottom side of spiral
#     for num in range(1, new_side_length):
#         spiral[y][x+num] = current_num
#         current_num += 1
#
#
# side_length = 9
# spiral = generate_spiral(side_length)
#
# # Repeatedly calculate ratio of primes to diagonal numbers for
# # increasing sizes of spiral until ratio < 10%
# while True:
#     nums_along_diagonals = (2 * side_length) - 1
#     num_primes = 0
#
#     for i in range(side_length):
#         if is_prime(spiral[i][i]):
#             num_primes += 1
#
#         if is_prime(spiral[i][side_length-i-1]):
#             num_primes += 1
#
#     percentage_ratio = 100 * (num_primes/nums_along_diagonals)
#
#     if percentage_ratio < 10:
#         print(side_length)
#         exit()
#
#     extend_spiral(spiral)
#     side_length += 2
#     print(side_length)

