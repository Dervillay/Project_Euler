# Begin at first value to have a cube with at least 3 digits
# (i.e. allowing for at least 5 permutations)
n = 5

# Dictionary to count how many cubes with a certain permutation exist
# key -> perm in ascending order
# value -> [number of cubes that are perms of this key, first cube that generated this key]
perms = {}

# Continue to increment n until solution is found
while True:

    # Calculate new cube and add to dictionary
    cube = n**3
    perm = "".join(sorted(str(cube)))

    # If this perm already exists, increment count by 1
    if perm in perms:
        perms[perm][0] += 1

        # If 5 found, print the lowest perm that generated this key and exit
        if perms[perm][0] == 5:
            print(perms[perm][1])
            exit()

    # Else, initialise count and store cube
    else:
        perms[perm] = [1, cube]

    n += 1

