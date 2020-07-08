i = 1

# Q & D brute force approach on increasing integers from 1
while True:
    i_digits = sorted(list(str(i)))
    i2_digits = sorted(list(str(i*2)))
    i3_digits = sorted(list(str(i*3)))
    i4_digits = sorted(list(str(i*4)))
    i5_digits = sorted(list(str(i*5)))
    i6_digits = sorted(list(str(i*6)))

    if i_digits == i2_digits and i2_digits == i3_digits and \
       i3_digits == i4_digits and i4_digits == i5_digits and \
       i5_digits == i6_digits:
        print(i)
        exit()

    i += 1

