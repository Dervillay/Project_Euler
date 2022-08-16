# Calculate number of rectangles in an M x N grid
# by summing the number of possible positions
# for each size of rectangle up to M x N
def num_rectangles(m, n):
    total = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            h_positions = m - i + 1
            v_positions = n - j + 1
            total += h_positions * v_positions
    return total

target_rects = 2000000
closest_area = 0
closest_num_rects = 0

# Print the area of the grid with the number of rectangles closest to target_rects
for x in range(1, 100):
    for y in range(1, 100):
        rects = num_rectangles(x, y)

        if abs(target_rects - rects) < abs(target_rects - closest_num_rects):
            closest_num_rects = rects
            closest_area = x * y

print(closest_area)
