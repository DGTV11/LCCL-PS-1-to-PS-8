I_s = list()

while True:
    inp = input("Input something (end by entering nothing): ")
    if inp == str():
        break
    else:
        I_s.append(inp)

O_s = list()

for item in I_s:
    if item not in O_s:
        O_s.append(item)

for item in O_s:
    print(item)