triangle_nums = [int(0.5*n*(n+1)) for n in range(1, 30)]
letter_vals = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
triangle_words = 0

with open('words.txt', 'r') as f:
    words = [w.replace("\"", "") for w in f.read().split(',')]

for word in words:
    word_val = 0

    for letter in word:
        word_val += letter_vals[letter]

    if word_val in triangle_nums:
        triangle_words += 1

print(triangle_words)