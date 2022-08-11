# Implementation of A* search heavily inspired by pseudocode here:
# https://en.wikipedia.org/wiki/A*_search_algorithm

from collections import defaultdict

with open('matrix.txt', 'r') as f:
    filelines = f.read().splitlines()

matrix = []
for line in filelines:
    row = [int(i) for i in line.split(',')]
    matrix.append(row)
len_matrix = len(matrix)

# Decode string encoding of positional information
# e.g. turn '6,9' into [6, 9]
def decode(pos):
    return [int(p) for p in pos.split(',')]

# Use came_from to reconstruct the path to a node and return the path sum
def reconstruct_path_and_return_sum(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path = [current] + total_path

    total_sum = 0
    for pos in total_path:
        i, j = [int(p) for p in pos.split(',')]
        total_sum += matrix[i][j]

    return total_sum


# Use manhattan distance to bottom right as heuristic
def h(pos):
    i, j = decode(pos)
    return 2 * 79 - i - j


# Helper to return the encoded positions of a position's neighbours
def get_neighbours(pos):
    neighbours = []
    i, j = decode(pos)
    if i > 0:
        neighbours.append(f'{i-1},{j}')
    if i < len_matrix-1:
        neighbours.append(f'{i+1},{j}')
    if j > 0:
        neighbours.append(f'{i},{j-1}')
    if j < len_matrix-1:
        neighbours.append(f'{i},{j+1}')

    return neighbours

current = '0,0'  # Encode positions as strings to allow use as keys of dicts
open_set = {current: h(current)}
came_from = {}
g_score = defaultdict(lambda: float('inf'))
g_score[current] = 0

f_score = defaultdict(lambda: float('inf'))
f_score[current] = h(current)

while open_set:
    current = min(open_set, key=open_set.get)
    if current == '79,79':
        print(reconstruct_path_and_return_sum(came_from, current))
        break
    
    del open_set[current]

    neighbours = get_neighbours(current)
    for neighbour in neighbours:
        n_i, n_j = decode(neighbour)
        tentative_g_score = g_score[current] + matrix[n_i][n_j]
        
        if tentative_g_score < g_score[neighbour]:
            came_from[neighbour] = current
            g_score[neighbour] = tentative_g_score
            f_score[neighbour] = tentative_g_score + h(neighbour)

            if neighbour not in open_set:
                open_set[neighbour] = f_score[neighbour]

    
    
    