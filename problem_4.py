from math import floor

palindromes = []

for i in range(999, 99, -1):
    for j in range(999, 99, -1):

        product = str(i * j)
        palindrome = True

        for n in range(floor(len(product)/2)):
            if product[n] != product[-n-1]:
                palindrome = False
                break

        if palindrome == True:
            palindromes.append(int(product))

print(max(palindromes))


