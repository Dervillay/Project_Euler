# Current number to write
i = 1
# Current n value
n = 2

# Construct 1001 * 1001 grid to store spiral
grid = [[0 for x in range(1001)] for y in range(1001)]

# Initial coordinates of center of spiral
x = 500
y = 500

# Initialise center of spiral to 1
grid[y][x] = 1
i += 1

# Draw each (N+1) x (N+1) square of the spiral up to 1001
while n < 1001:
    x += 1

    # Draw right side of spiral
    for num in range(n):
        grid[y+num][x] = i
        i += 1

    y += n-1

    # Draw bottom side of spiral
    for num in range(1, n+1):
        grid[y][x-num] = i
        i += 1

    x -= n

    # Draw left side of spiral
    for num in range(1, n+1):
        grid[y-num][x] = i
        i += 1

    y -= n

    # Draw top side of spiral
    for num in range(1, n+1):
        grid[y][x+num] = i
        i += 1

    x += n
    n += 2

# Initialise sum_diagonals as -1 to account for counting the central 1 twice
sum_diagonals = -1

for n in range(1001):
    sum_diagonals += grid[n][n]
    sum_diagonals += grid[1000-n][n]

print(sum_diagonals)