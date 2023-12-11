from random import randint
largest = randint(1, 100)
print(largest)

updates = 0
for i in range(99):
    x = randint(1, 100)
    print(x, end=' ')
    if x > largest: 
        largest = x
        print('<== Update')
        updates += 1
    else:
        print()

print(f'The maximum value found was {largest}')
print(f'The maximum value found was updated {updates} times')