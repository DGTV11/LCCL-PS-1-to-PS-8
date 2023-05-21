from int_hex import hex2int, int2hex, IntHexTable


def arb2int(basein, valin):  # str
    basein = int(basein)
    if (basein < 2) or (basein > 16):
        raise ValueError("Invalid base!")
    n = list(str(valin))
    n.reverse()
    out = int()
    for i, char in enumerate(n):
        x = hex2int(str(char))
        if x >= basein:
            raise ValueError("Invalid base!")
        out += x * (basein**i)
    return out


def int2arb(baseout, valin):  # int
    n = int(valin)
    out = str()
    baseout = int(baseout)
    if (baseout < 2) or (baseout > 16):
        raise ValueError("Invalid base!")
    q = 1
    while q != 0:
        q = n // baseout
        r = n % baseout
        out += IntHexTable[r]
        n = q
    return out[::-1]


def arb2arb(basein, baseout, valin):  # str
    return int2arb(baseout, arb2int(basein, valin))

if __name__ == "__main__":
    while True:
        x = int(input('''
        1) arbitrary base to base-10
        2) base-10 to arbitrary base
        3) arbitrary base to arbitrary base
        
        >>> '''))
        if x == 1:
            b = int(input("Please input the input base (2-16): "))
            i = input("Please input the number to be converted: ")
            print(f"INPUT NUMBER (BASE {b}): {i}")
            print(f"OUTPUT NUMBER (BASE 10): {arb2int(b, i)}")
        elif x == 2:
            b = int(input("Please input the output base (2-16): "))
            i = int(input("Please input the number to be converted: "))
            print(f"INPUT NUMBER (BASE 10): {i}")
            print(f"OUTPUT NUMBER (BASE {b}): {int2arb(b, i)}")
        elif x == 3:
            b1 = int(input("Please input the input base (2-16): "))
            b2 = int(input("Please input the output base (2-16): "))
            i = input("Please input the number to be converted: ")
            print(f"INPUT NUMBER (BASE {b1}): {i}")
            print(f"OUTPUT NUMBER (BASE {b2}): {arb2arb(b1, b2, i)}")