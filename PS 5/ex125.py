from random import choice, randint

SUITS = ('s', 'h', 'd', 'c')
VALUES = ('1', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
#VALUES = tuple(range(1,10)) + ('T', 'J', 'Q', 'K', 'A')

print(VALUES)
def createDeck():
    deck = list()
    for suit in SUITS:
        for val in VALUES:
            #deck.append(str(val)+suit)
            deck.append(val+suit)
    return deck

def shuffle(_list): #bogosort thig I found on the internet
    n = len(_list)
    for i in range(0, n):
        r = randint(0, n-1)
        _list[i], _list[r] = _list[r], _list[i]
    return _list

if __name__ == '__main__':
    d = createDeck()
    print(d)
    print(shuffle(d))