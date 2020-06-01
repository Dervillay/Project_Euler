from math import factorial

# Gives num of paths along edges from top left to bottom right in X * Y grid
# Does this by recursively calculating numbers from Pascal's triangle
def num_paths(x, y):
    if x == 0 and y == 0:
        return 0
    elif x == 0 or y == 0:
        return 1
    else:
        return num_paths(x-1, y) + num_paths(x, y-1)

# However, a more efficient solution is to implement a function that calculates nCr directly
def choose(n, r):
    return int(factorial(n)/(factorial(r)*factorial(n-r)))

# Num of paths in an N * N grid is just 2N choose N
print(choose(40, 20))
