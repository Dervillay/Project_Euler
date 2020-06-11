cur_num = 1
prev_num = 1
index = 2

while len(str(cur_num)) < 1000:
    new_num = cur_num + prev_num
    prev_num = cur_num
    cur_num = new_num

    index += 1

print(index)