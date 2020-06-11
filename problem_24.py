from itertools import permutations

perms = list(permutations(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]))

perms = sorted([int(''.join(x)) for x in perms])

print(perms[999999])

