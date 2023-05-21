from ex125 import createDeck, shuffle

def deal(noOfHands, cardsPerHand, deck):
    handlist = list()
    for i in range(noOfHands):
        handlist.append(list())
    
    for i in range(cardsPerHand):
        for i in range(len(handlist)):
            handlist[i].append(deck[0])
            deck = deck[1:]

    return handlist, deck

if __name__ == '__main__':
    dec = shuffle(createDeck())
    handlist, deck = deal(4, 5, dec)
    for hand in handlist:
        print(hand)
    print(deck)