def _filter(l):
    lx = list()
    for item in l:
        if item not in lx:
            lx.append(item)
    return lx

if __name__ == '__main__':
    l = list()
    while True:
        x = input('Input word: ')
        if x.strip() == '':
            break
        l.append(x)
    for item in _filter(l):
        print(item)