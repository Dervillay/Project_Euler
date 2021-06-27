with open('matrix.txt', 'r') as f:
    filelines = f.read().splitlines()

matrix = []
for line in filelines:
    row = [int(i) for i in line.split(',')]
    matrix.append(row)
len_matrix = len(matrix)

min_path_sums = [[-1 for j in range(len_matrix)] for i in range(len_matrix)]

# Initialise min_path_sums with end-column values
for i in range(len_matrix):
    min_path_sums[i][-1] = matrix[i][-1]

# Populate min_path sums from second-last column to first
for j in range(len_matrix-2, -1, -1):

    # Down sweep (finding min sum of rightward path and downward path)
    min_path_sums[0][j] = matrix[0][j] + min_path_sums[0][j+1]
    for i in range(1, len_matrix):
        min_path_sums[i][j] = matrix[i][j] + min(min_path_sums[i][j+1], min_path_sums[i-1][j])

    # Up sweep (finding min sum of current path and upwards path)
    for i in range(len_matrix-2, -1, -1):
        min_path_sums[i][j] = min(matrix[i][j] + min_path_sums[i+1][j], min_path_sums[i][j])

first_col_sums = [min_path_sums[i][0] for i in range(len_matrix)]
print(min(first_col_sums))