from math import factorial

# Return the result of summing the factorial of each of n's digits
def fact_digits(n):
    total = 0
    digits = [int(i) for i in str(n)]

    for i in digits:
        total += factorial(i)

    return total

# Memoized dictionary to store the sequence length for each initial value
repeating_nums = {}

# Initialise counter for sequences of length 60
total = 0

# Iterate through all n below 1,000,000
for n in range(1000000):
    num_terms = 1
    nums = [n]

    # Generate the sequence and count its length until
    # either it yields a number in repeating_nums, or reaches
    # a length of 61
    while num_terms < 61:
        new_num = fact_digits(nums[-1])

        # If the remaining length is known, add this
        # to the current length and break
        if new_num in repeating_nums:
            num_terms += repeating_nums[new_num]
            break

        # Detect repeated numbers in the sequence and break
        elif new_num in nums:
            break

        # Otherwise continue
        else:
            nums.append(new_num)
            num_terms += 1

    # Store n's sequence length in memoized dictionary
    repeating_nums[n] = num_terms

    # Increment total if sequence length is 60
    if num_terms == 60:
        total += 1

print(total)


