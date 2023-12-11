from random import randint

def gen():
    return randint(1, 100)

maxno = gen()
chgs = 0

for i in range(1, 99):
    no = gen()
    if no > maxno:
        maxno = no
        print(f'{maxno} <== Update')
        chgs += 1
    else:
        print(no)

print(f"""
The maximum value found was {maxno}
The maximum value was updated {chgs} times
""")