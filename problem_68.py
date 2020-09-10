# The approach taken to solve this problem was to maximise the
# outer digits by setting them to 10, 9, 8, 7 and 6, and then
# to fill out the rest by hand via trial and error

# Since we know that numbers 6-10 will appear on the outer nodes,
# 1-5 will appear on the inner nodes, with each of these inner nodes counted twice.
# Therefore we can find what each straight line must sum to:
# 2*(1+2+3+4+5) + (6+7+8+9+10) = 70
# 70/5 = 14
# so each triplet must sum to 14

# Working this through by hand, we obtain:
# 6,5,3;10,3,1;9,1,4;8,4,2;7,2,5
# Since the counting must start on the smallest number amongst the outer nodes,
# which in our case is 6, and we maximise the outer number as we move clockwise
# around the ring.

# Since we must count from 6 clockwise and we have maximised
# the outer nodes, this must already be a maximum solution.
# Our solution is 16 digits long too, satisfying the required answer.

print(6531031914842725)
