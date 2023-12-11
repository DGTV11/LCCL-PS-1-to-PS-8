'''
Let result be an empty string
Let q represent the number to convert 
repeat until q is 0
    Set r equal to the remainder when q is divided by 2
    Convert r to a string and add it to the beginning of result
    Divide q by 2, discarding any remainder, and store the result back into q
'''

def b10tob2(q: int, res: str='') -> str:
    if q == 0:
        return res
    r = q % 2
    res = str(r) + res
    return b10tob2(q // 2, res)

q = int(input('Plz input number to convert into binary: '))
print(f'The above decimal number is {b10tob2(q)} in binary.')