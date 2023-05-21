F2F = 10.5

hy = float(input('Dog years: '))
if hy < 0:
    raise ValueError('Inputted negative number')
elif hy <= 2:
    print(f'{hy} human years is {hy*F2F} in dog years')
else:
    print(f'{hy} human years is {(2*F2F)+((hy-2)*4)} in dog years')