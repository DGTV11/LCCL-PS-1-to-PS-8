l = list()
while True:
    x = input('Input word: ')
    if x.strip() == '':
        break
    l.append(int(x))

ln = list()
lo = list()
lp = list()
for item in l:
    if item < 0: ln.append(item)
    elif item == 0: lo.append(item)
    elif item > 0: lp.append(item)

for item in ln + lo + lp:
    print(item)