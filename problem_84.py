from collections import Counter, defaultdict
from random import randint

num_sides = 4
num_trials = 1000000
num_spaces = 40
spaces_visited = defaultdict(int)

# Helpful lookups for numbers corresponding to spaces
community_chests = [2, 17, 33]
chances = [7, 22, 36]
railways = [5, 15, 25, 35]
utilities = [12, 28]

def roll_dice():
    return randint(1, num_sides), randint(1, num_sides)

def move_spaces(curr_space, roll_sum):
    curr_space = (curr_space + roll_sum) % num_spaces

    # Handle landing on chances
    if curr_space in chances:
        num = randint(1, 16)
        if num == 1:
            curr_space = 0
        elif num == 2:
            curr_space = 10
        elif num == 3:
            curr_space = 11
        elif num == 4:
            curr_space = 24
        elif num == 5:
            curr_space = 39
        elif num == 6:
            curr_space = 5
        elif num in [7, 8]:
            while curr_space not in railways:
                curr_space = (curr_space + 1) % num_spaces
        elif num == 9:
            while curr_space not in utilities:
                curr_space = (curr_space + 1) % num_spaces
        elif num == 10:
            curr_space -= 3

    # Handle landing on community chests
    if curr_space in community_chests:
        num = randint(1, 16)
        if num == 1:
            curr_space = 0
        elif num == 2:
            curr_space = 10

    # Handle go to jail
    if curr_space == 30:
        curr_space = 10

    # Handle regular rolls
    return curr_space
    
# Run trials and print results
for _ in range(num_trials):
    double_count = 0
    current_space = randint(0, num_spaces-1)

    d1, d2 = roll_dice()
    current_space = move_spaces(current_space, d1 + d2)

    # Handle rolling doubles
    while d1 == d2:
        double_count += 1

        # Go to jail if three doubles rolled
        if double_count == 3:
            current_space = 10
            break

        d1, d2 = roll_dice()
        current_space = move_spaces(current_space, d1 + d2)

    spaces_visited[current_space] += 1

space_counter = Counter(spaces_visited)
print(space_counter.most_common(10))
print(''.join([f'{num:02}' for num, val in space_counter.most_common(3)]))