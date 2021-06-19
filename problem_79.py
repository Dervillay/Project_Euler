with open('keylog.txt', 'r') as f:
    logins = f.read().splitlines()

# Initial guess as concatenation of first two logins
passcode = ['3', '1', '9', '6', '8', '0']

for login_digits in logins:

    if login_digits[0] not in passcode:
        passcode.insert(0, login_digits[0])
    first_digit_index = passcode.index(login_digits[0])

    if login_digits[1] not in passcode:
        passcode.insert(first_digit_index + 1, login_digits[1])
    second_digit_index = passcode.index(login_digits[1])

    if login_digits[2] not in passcode:
        passcode += login_digits[2]
    third_digit_index = passcode.index(login_digits[2])

    if first_digit_index > third_digit_index:
        passcode[first_digit_index], passcode[third_digit_index] = passcode[third_digit_index], passcode[first_digit_index]
        first_digit_index, third_digit_index = third_digit_index, first_digit_index

    if first_digit_index > second_digit_index:
        passcode[first_digit_index], passcode[second_digit_index] = passcode[second_digit_index], passcode[first_digit_index]
        first_digit_index, second_digit_index = second_digit_index, first_digit_index

    if second_digit_index > third_digit_index:
        passcode[second_digit_index], passcode[third_digit_index] = passcode[third_digit_index], passcode[second_digit_index]
        second_digit_index, third_digit_index = third_digit_index, second_digit_index

print(''.join(passcode))
