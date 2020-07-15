with open('p059_cipher.txt', 'r') as f:
    encrypted_ascii_codes = [int(n) for n in f.read().split(',')]

def attempt_decrypt(key):
    key_ascii_codes = [ord(n) for n in key]
    decrypted_ascii_codes = []
    decrypted_characters = []

    for i in range(0, len(encrypted_ascii_codes), 3):
        for j in range(3):
            decrypted_ascii_codes.append(key_ascii_codes[j] ^ encrypted_ascii_codes[i+j])

    for i in range(len(decrypted_ascii_codes)):
        decrypted_characters.append(chr(decrypted_ascii_codes[i]))

    decrypted_message = "".join(decrypted_characters)

    return decrypted_message, decrypted_ascii_codes


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Cycle through potential encryption keys and attempt to decrypt
for i in letters:
    for j in letters:
        for k in letters:
            key = i + j + k
            decrypted_message, decrypted_ascii_codes = attempt_decrypt(key)

            # If the common word 'the' surrounded by spaces is found in an attempted
            # decryption then calculate and return the sum of this message's ASCII values
            if ' the ' in decrypted_message:
                total = 0
                
                for code in decrypted_ascii_codes:
                    total += code

                print(total)
                exit()