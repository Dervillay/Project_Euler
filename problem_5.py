curr = 2520

found = False

while not found:
    found = True

    for i in range(1, 21):
        if curr % i != 0:
            found = False
            break

    if found:
        print(curr)
    else:
        curr += 20