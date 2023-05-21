ints = input('Input 3 integers, with spaces seperating them: ').split()
if len(ints) != 3:
    raise NotImplementedError('Unable to sort less or more than 3 integers!')

for i in range(len(ints)):
    ints[i] = int(ints[i])
min_int = min(ints)

max_int = max(ints)

sum = 0
for i in range(len(ints)):
    sum += ints[i]
med_int = sum-(min_int+max_int)

sum = None

sorted_ints = [min_int, med_int, max_int]

print(f'''
- Unsorted integers: {ints}
- Sorted integers (from smallest to largest): {sorted_ints}
''')