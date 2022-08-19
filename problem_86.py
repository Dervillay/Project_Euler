from math import sqrt

# Calculate length of shortest corner-to-corner path for given H x W x D cuboid
# using formula from https://math.stackexchange.com/questions/1189743/minimum-distance-to-reach-opposite-corner
def shortest_path_length(w, h_plus_d):
    return sqrt(w**2 + h_plus_d**2)

"""
- We have that min_dist**2 = (h+d)**2 + w**2
- we continually increment w, using it to represent the current value of M,
 and see how many integer solutions we can find for 1 <= h+d <= 2w
- once we find an integer solution, we can calculate the number of possible unique values for h and d
(which is the number of cuboids that have this corner-to-corner distance)
- if h + d <= w, we have floor(h + d / 2) combinations of possible values for h + d
- else we have 1 + (w - floor((h + d + 1)/2)) combinations of possible values for h + d
"""

w = 0
num_integer_solutions = 0
target_integer_solutions = 1000000

while num_integer_solutions < target_integer_solutions:
    w += 1
    for h_plus_d in range(1, 2*w + 1):
        if shortest_path_length(w, h_plus_d).is_integer():
            if h_plus_d <= w:
                num_integer_solutions += h_plus_d // 2
            else:
                num_integer_solutions += 1 + (w - (h_plus_d + 1) // 2)

print(w)
