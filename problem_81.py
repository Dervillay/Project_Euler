with open('matrix.txt', 'r') as f:
    filelines = f.read().splitlines()

matrix = []
for line in filelines:
    row = [int(i) for i in line.split(',')]
    matrix.append(row)
len_matrix = len(matrix)

min_path_sums = [[-1 for j in range(len_matrix)] for i in range(len_matrix)]

# Return minimal path sum starting from position i, j
def minimal_path_sum(i, j):

    if min_path_sums[i][j] != -1:
        return min_path_sums[i][j]

    elif i == j == len_matrix-1:
        min_sum = matrix[i][j]

    elif i == len_matrix-1:
        min_sum = matrix[i][j] + minimal_path_sum(i, j+1)

    elif j == len_matrix-1:
        min_sum = matrix[i][j] + minimal_path_sum(i+1, j)

    else:
        right_path_sum = minimal_path_sum(i, j+1)
        down_path_sum = minimal_path_sum(i+1, j)
        min_sum = matrix[i][j] + min(right_path_sum, down_path_sum)

    min_path_sums[i][j] = min_sum
    return min_sum

print(minimal_path_sum(0, 0))