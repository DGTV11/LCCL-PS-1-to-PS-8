from ex146 import makeCard, showCard
from ex147 import checkCard
from ex136 import reverseLookup
from random import sample

def callCard(card, callNo):
    cX = card
    for column in cX.values():
        cK = reverseLookup(cX, column)[0]
        for i, number in enumerate(column):
            if number == callNo:
                cX[cK][i] = 0
    return cX

POSS_CALLS = list(range(1, 76))
calls = list()
for i in range(1000):
    card = makeCard()
    callsx = 0
    pc = sample(POSS_CALLS, len(POSS_CALLS))
    while not checkCard(card):
        card = callCard(card, pc[-1])
        pc.pop()
        callsx += 1
    calls.append(callsx)

print(f'''
Minimum calls: {min(calls)}
Maximum calls: {max(calls)}
Average calls: {sum(calls)/1000}
''')