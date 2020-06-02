triangle = [[75],
            [95, 64],
            [17, 47, 82],
            [18, 35, 87, 10],
            [20, 4, 82, 47, 65],
            [19, 1, 23, 75, 3, 34],
            [88, 2, 77, 73, 7, 63, 67],
            [99, 65, 4, 28, 6, 16, 70, 92],
            [41, 41, 26, 56, 83, 40, 80, 70, 33],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40,31],
            [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

triangle_len = len(triangle)

#################################################################################
# Carry out an A* search, where the heuristic is the sum of the greedy completion
#################################################################################

# Return sum of path elements so far
def g(path):
    return sum(path)


# Return heuristic value of node
def h(path):
    path_len = len(path)

    # If goal node, return 0
    if path_len == triangle_len:
        return 0

    # Else find the sum of the greedy completion
    path = [path[-1]]
    i = triangle[path_len-1].index(path[-1])

    while path_len < triangle_len:
        left = triangle[path_len][i]
        right = triangle[path_len][i+1]

        if left > right:
            path.append(left)
        else:
            path.append(right)
            i += 1
        path_len += 1

    return sum(path)

# Define a dictionary to store fringe nodes
fringe = {}

node_id = 0

# We define a node as a dict where:
# 0th element is path,
# 1st element is g(node),
# 2nd element is h(node),
# 3rd element is f(node) = g(node) + h(node)
start_node = {0:[75], 1: 75, 2: 1064, 3: 75 + 1064}

fringe[node_id] = start_node

# While fringe nodes exist or until an optimal solution is found, run
while fringe:
    # Get node with maximum f value
    node = fringe.pop(max(fringe, key=lambda x: fringe[x][3]))

    # If optimal solution is found, return its path length
    if len(node[0]) == triangle_len and h(node[0]) == 0:
        print(node[3])
        exit()

    # Get index (in triangle) of last node in current node's path
    index = triangle[len(node[0])-1].index(node[0][-1])

    # Get length of current node's path
    path_len = len(node[0])

    # Copy path twice to avoid both pointing to the original list
    left_path = node[0][:]
    right_path = node[0][:]

    # Create left and right child-nodes
    left_path.append(triangle[path_len][index])
    right_path.append(triangle[path_len][index+1])

    g_left = g(left_path)
    g_right = g(right_path)

    h_left = h(left_path)
    h_right = h(right_path)

    f_left = g_left + h_left
    f_right = g_right + h_right

    left_node = {0: left_path, 1: g_left, 2: h_left, 3: f_left}
    right_node = {0: right_path, 1: g_right, 2: h_right, 3: f_right}

    # Add new nodes to fringe with unique ids
    node_id += 1
    fringe[node_id] = left_node
    node_id += 1
    fringe[node_id] = right_node