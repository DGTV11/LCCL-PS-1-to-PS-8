def simplestForm(n, d):
    x = min(n, d)

    while (n % x != 0) or (d % x != 0):
        x -= 1
    
    return n // x, d // x
    
if __name__ == '__main__':
    num = abs(int(input("Numerator: ")))
    denom = abs(int(input("Denominator: ")))
    no, do = simplestForm(num, denom)
    print(f"{num}/{denom} = {no}/{do}")