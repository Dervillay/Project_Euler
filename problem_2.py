def fib_list(up_to):
    fib_list = [1]
    last_num = 2

    while last_num < up_to:
        fib_list.append(last_num)
        last_num = fib_list[-1] + fib_list[-2]

    return fib_list

sum = 0

for i in fib_list(4000000):
    if i % 2 == 0:
        sum += i

print(sum)