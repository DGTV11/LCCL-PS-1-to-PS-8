binstr = list(input("Plz input binary string: "))
rbinstr = list()
for item in binstr:
    rbinstr.insert(0, item)

i = 1
n = 0

for item in rbinstr:
    currN = int(item)
    if currN == 1:
        n += currN*i
    i *= 2

print(f'The above binary number is {n} in decimal.')