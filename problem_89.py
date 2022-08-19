with open('roman.txt') as f:
    numbers = f.read().splitlines()

numeral_vals = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1
}

def minimal_numerals(numerals):
    # Find the denary value of numerals
    total = 0
    for i in range(len(numerals)):
        prev_numeral_val = numeral_vals[numerals[i-1]] if i > 0 else 1001
        curr_numeral_val = numeral_vals[numerals[i]]
        next_numeral_val = numeral_vals[numerals[i+1]] if i < len(numerals) - 1 else 0

        # Handle subtractive numerals (e.g. IV, XC)
        if next_numeral_val > curr_numeral_val:
            total += (next_numeral_val - curr_numeral_val)

        # Only add current numeral's value if previous numeral wasn't subtractive
        elif prev_numeral_val >= curr_numeral_val:
            total += curr_numeral_val

    # Convert the denary value into its minimal numeral form
    minimal = ''
    for numeral, val in numeral_vals.items():
        while total - val >= 0:
            minimal += numeral
            total -= val

    return minimal

# Calculate how many characters can be saved by minimising all given numbers
characters_saved = 0
for number in numbers:
    characters_saved += len(number) - len(minimal_numerals(number))

print(characters_saved)
