with open('names.txt', 'r') as f:
    names = [n.replace("\"", "") for n in f.read().split(',')]

score = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

names = sorted(names)

total = 0

for i in range(len(names)):
    i_score = 0

    for j in names[i]:
        i_score += score[j]

    total += i_score * (i+1)

print(total)