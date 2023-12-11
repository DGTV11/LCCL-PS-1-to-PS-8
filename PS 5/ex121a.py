'''
In order to win the top prize in a particular lottery, one 
must match all 6 numbers on his or her ticket to the 6 numbers 
between 1 and 49 that are drawn by the lottery organizer. 
Write a program that generates a random selection of 6 numbers 
for a lottery ticket. Ensure that the 6 numbers selected do 
not contain any duplicates. Display the numbers in ascending 
order.
'''
from random import randrange

nums = list()
for i in range(6):
    while True:
        n = randrange(1, 49)
        if n not in nums:
            break
    nums.append(n)

nums = sorted(nums)

for i in range(6):
    print(nums[i], end = " ")
print()