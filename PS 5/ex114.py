I_s = list()

while True:
    inp = input("Input any integer (even negatives) (end by entering nothing): ")
    if inp == str():
        break
    else:
        I_s.append(int(inp))

n = list()
z = list()
p = list()

for item in I_s:
    if item < 0:
        n.append(item)
    elif item == 0:
        z.append(item)
    elif item > 0:
        p.append(item)

for item in n + z + p:
    print(item)

# In: 3, -4, 1, 0, -1, 0, -2
# Out: -4, -1, -2, 0, 0, 3, 1