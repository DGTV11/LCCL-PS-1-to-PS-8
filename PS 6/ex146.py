from random import sample

# B 01 - 15
# I 16 - 30
# N 31 - 45
# G 46 - 60
# O 61 - 75

def makeCard():
    bd = {
        'B' : sample(range(1, 15), 5),
        'I' : sample(range(16, 30), 5),
        'N' : sample(range(31, 45), 5),
        'G' : sample(range(46, 60), 5),
        'O' : sample(range(61, 75), 5)
    }
    return bd

def showCard(card):
    print(f'B  I  N  G  O')
    for i in range(5):
        print(f'{card["B"][i]:0>2} {card["I"][i]:0>2} {card["N"][i]:0>2} {card["G"][i]:0>2} {card["O"][i]:0>2}')

if __name__ == '__main__':
    showCard(makeCard())