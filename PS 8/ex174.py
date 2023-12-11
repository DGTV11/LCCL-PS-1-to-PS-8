import sys

isInt = lambda n: type(n) is int

def GCD(a: int, b: int) -> int:
    if not isInt(a): raise ValueError
    if not isInt(b): raise ValueError
    if b == 0:
        return a
    c = a % b
    return GCD(b, c)

if __name__ == '__main__':
    while True:
        a = int(input('Please input first integer: '))
        b = int(input('Please input second integer: '))
        print(f'Greatest common demoninator {GCD(a, b)}')