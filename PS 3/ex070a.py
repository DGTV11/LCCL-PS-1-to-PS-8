CONVERTION_TABLE = {
    1 : "a",
    2 : "b",
    3 : "c",
    4 : "d",
    5 : "e",
    6 : "f",
    7 : "g",
    8 : "h",
    9 : "i",
    10 : "j",
    11 : "k",
    12 : "l",
    13 : "m",
    14 : "n",
    15 : "o",
    16 : "p",
    17 : "q",
    18 : "r",
    19 : "s",
    20 : "t",
    21 : "u",
    22 : "v",
    23 : "w",
    24 : "x",
    25 : "y",
    26 : "z"
}

def GetKey(val):
    for key, value in CONVERTION_TABLE.items():
        if val == value:
            return key
    return "key doesn't exist"

key = int(input('Key: (positive key -> encode, negative key -> decode): '))
plaintext = list(input('Plaintext: '))

ciphertext = ""

for item in plaintext:
    if not item.lower() in CONVERTION_TABLE.values():
        ciphertext = ciphertext + item

    else:
        num = GetKey(item.lower())
        num += key
        while num < 1 or num > 26:
            if num < 1:
                num += 26
            elif num > 26:
                num -= 26

        if item.isupper():
            ciphertext = ciphertext + CONVERTION_TABLE[num].upper()
        else:
            ciphertext = ciphertext + CONVERTION_TABLE[num]

print(f'Ciphertext: {ciphertext}')