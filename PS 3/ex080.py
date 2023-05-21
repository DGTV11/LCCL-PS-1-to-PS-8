from random import randint

def flip():
    return randint(0, 1)

lenny = list()
for i in range(10):
    outcomes = list()
    iters = 0
    while True:
        outcomes.append(flip())
        if iters >= 3 and outcomes[-1] == outcomes[-2] == outcomes[-3]:
            break
        iters += 1

    for item in outcomes:
        if item == 1:
            print('H', end=' ')
        else:
            print('T', end=' ')

    lenny.append(len(outcomes))
    print(f"({lenny[-1]} flips)\n")

total = sum(lenny)

'''
total = 0
for item in lenny:
    total += item
'''

print(f'On average, {total/len(lenny)} flips were needed.')