from math import sqrt, ceil

def pDivs(n):
    n = int(n)
    i = 1
    divs = list()
    midp = ceil(sqrt(n))
    while i != midp:
        if n % i == 0:
            divs.append(i)
            divs.append(n // i)
        i += 1
    return sorted(divs)

if __name__ == '__main__':
    n = int(input("Please input an integer: "))

    print(f"Factors of {n}:")
    d = pDivs(n)
    for num in d:
        print(num)