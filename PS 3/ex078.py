'''
Let result be an empty string
Let q represent the number to convert 
repeat until q is 0
    Set r equal to the remainder when q is divided by 2
    Convert r to a string and add it to the beginning of result
    Divide q by 2, discarding any remainder, and store the result back into q
'''

result = ""
q = int(input('Plz input number to convert into binary: '))

while q != 0:
    r = q % 2
    result = str(r) + result
    q = q // 2

print(f'The above decimal number is {result} in binary.')