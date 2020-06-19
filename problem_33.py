from fractions import Fraction

num_product = 1
denom_product = 1

# Quick and dirty brute force solution. I'm not proud.
for denominator in range(10, 100):

    for numerator in range(10, denominator):
        str_denom = str(denominator)
        str_num = str(numerator)
        common_digit = [x for x in str_denom if x in str_num]

        if common_digit:
            common_digit = common_digit[0]
        else:
            continue

        if common_digit != '0':
            denom = int(str_denom.replace(common_digit, '', 1))
            num = int(str_num.replace(common_digit, '', 1))

            if num != 0 and denom != 0 and num/denom == numerator/denominator:
                num_product *= numerator
                denom_product *= denominator

print(Fraction(num_product, denom_product).denominator)

