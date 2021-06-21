from decimal import Decimal, getcontext

# Set number of significant figures to 110 to prevent rounding errors
getcontext().prec = 110

perfect_squares = [i**2 for i in range(1, 11)]
total = 0

for i in range(1, 101):
    if i not in perfect_squares:
        decimal_string = str(Decimal(i).sqrt())
        decimal_digits = decimal_string[:1] + decimal_string[2:101]
        digital_sum = sum([int(d) for d in decimal_digits])

        total += digital_sum
        
print(total)