nums = list()
while True:
    inp = float(input('Enter a number to be averaged (enter 0 to stop input cycle): '))
    if inp == 0:
        break
    else:
        nums.append(inp)

print(f'All numbers: {nums}')

sum = 0
for item in nums:
    sum += item

print(f'Average of all numbers: {sum/len(nums)}')