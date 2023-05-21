from ex146 import makeCard, showCard
from random import choice, randint

def checkCard(card):
    for column in card.values():
        if sum(column) == 0:
            return True

    for i in range(0, 4):
        x = list()
        for column in card.values():
            x.append(column[i])
        if sum(x) == 0:
            return True

    x = list()
    for i, column in enumerate(card.values()):
        x.append(column[i])
    if sum(x) == 0:
        return True

    x = list()
    for i, column in enumerate(reversed(card.values())):
        x.append(column[i])
    if sum(x) == 0:
        return True

    return False

if __name__ == "__main__":
    card1 = makeCard()
    card1[choice(list(card1))] = [0] * 5
    showCard(card1)
    print(f'Bingo? {"Yes!" if checkCard(card1) else "No!"}')

    card2 = makeCard()
    x = randint(0, 4)
    for column in card2.values():
        column[x] = 0
    showCard(card2)
    print(f'Bingo? {"Yes!" if checkCard(card2) else "No!"}')

    card3 = makeCard()
    for i, column in enumerate(card3.values()):
        column[i] = 0
    showCard(card3)
    print(f'Bingo? {"Yes!" if checkCard(card3) else "No!"}')

    x = True
    card4 = makeCard()
    while x:
        y = card4
        for column in y.values():
            column[randint(0, 4)] = 0
        x = checkCard(y)
    showCard(y)
    print(f'Bingo? {"Yes!" if checkCard(y) else "No!"}')