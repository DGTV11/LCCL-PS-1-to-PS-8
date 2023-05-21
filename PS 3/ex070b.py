key = int(input('Key: (positive key -> encode, negative key -> decode): '))
plaintext = list(input('Plaintext: '))

ciphertext = ""

for item in plaintext:
    if not 97 <= ord(item.lower()) <= 122:
        ciphertext = ciphertext + item

    else:
        num = ord(item.lower()) - 96
        num += key
        while num < 1 or num > 26:
            if num < 1:
                num += 26
            elif num > 26:
                num -= 26

        if item.isupper():
            ciphertext = ciphertext + chr(num + 96).upper()
        else:
            ciphertext = ciphertext + chr(num + 96)

print(f'Ciphertext: {ciphertext}')