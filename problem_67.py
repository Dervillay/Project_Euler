triangle = []

# Populate triangle from file
with open('triangle.txt', 'r') as f:
    for line in f.read().splitlines():
        triangle.append([int(x) for x in line.split(' ')])

# Dynamic programming approach that solves the problem bottom up
len_triangle = len(triangle)
current_row = len_triangle - 2

# Starting from the penultimate row and moving up the triangle,
# add to each number the max of the two numbers below it
for row in range(len_triangle - 1):
    for i in range(len(triangle[current_row])):
        left = triangle[current_row+1][i]
        right = triangle[current_row+1][i+1]

        triangle[current_row][i] += max(left, right)

    # Remove last row and decrement current_row index
    del triangle[current_row+1]
    current_row -= 1

print(triangle[0][0])
