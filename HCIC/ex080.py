from random import choice

memory = list()

totalflips = 0
for x in range(10):
    i = 0
    while True:
        x = choice(['H', 'T'])
        print(x, end=' ')
        if memory != list() and x != memory[-1]:
            memory = [x]
        else:
            memory.append(x)
            if len(memory) == 3:
                print(f'({i} flips)')
                totalflips += i
                break
        i += 1

print(f'On average, {totalflips/10} were needed')
