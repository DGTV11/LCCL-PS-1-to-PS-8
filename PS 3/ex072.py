string = input('Please input string to be checked: ')

reversedstr = ""
for char in string:
    reversedstr = char + reversedstr

if string == reversedstr:
    print(f'{string} is a palindrome.')
else:
    print(f'{string} is not a palindrome as {string} is not equal to {reversedstr}.')