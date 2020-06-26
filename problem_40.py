product = 1
const = ""
vals = [1, 10, 100, 1000, 10000, 100000, 1000000]

d = 1

while d < 1000001:
    const += str(d)

    if d in vals:
        product *= int(const[d-1])

    d += 1

print(product)