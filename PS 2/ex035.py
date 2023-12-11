Ihy = float(input('Dog years: '))
if Ihy < 0:
    raise ValueError('Inputted negative number')

hy = Ihy
dy = 0

if hy >= 2:
    hy -= 2
    dy += 10.5*2
    if hy <= 0:
        print(f'{Ihy} human years is {dy} in dog years')
        quit()
else:
    dy += 10.5*Ihy
    print(f'{Ihy} human years is {dy} in dog years')
    quit()

dy += 4*hy
print(f'{Ihy} human years is {dy} in dog years')
hy = None
Ihy = None
dy = None