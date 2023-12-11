print(end=' '*4)
for i in range(1, 11):
    print(f'{i:4d}', end='')
print()

for x in range(1, 11):
    print(f'{x:4d}', end='')
    for i in range(1, 11):
        print(f'{i*x:4d}', end='')
    print()