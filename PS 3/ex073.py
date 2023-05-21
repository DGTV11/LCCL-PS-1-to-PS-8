USELESSSTUFFS = [" ", ".", ",", "?", "!"]

string = input('Please input string to be checked: ')

nstring = ""
for char in string:
    if char in USELESSSTUFFS:
        continue
    else:
        nstring = char.lower() + nstring

reversedstr = ""
for char in nstring:
    reversedstr = char + reversedstr

if nstring == reversedstr:
    print(f'{string} is a palindrome.')
else:
    print(f'{string} is not a palindrome.')