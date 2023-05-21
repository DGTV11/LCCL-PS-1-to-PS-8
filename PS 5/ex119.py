'''
Write a program that reads numbers from the user until a blank 
line is entered. Your program should display the average of 
all of the values entered by the user. Then the program should 
display all of the below average values, followed by all of 
the average values (if any), followed by all of the above 
average values. An appropriate label should be displayed 
before each list of values.
'''

nums = list()
n = input("Please input a number (blank to stop): ")
while n != str(): 
    nums.append(float(n))
    n = input("Please input a number (blank to stop): ")

try:  
    aveNum = sum(nums)/len(nums)
    blwAveNums = list()
    aveNums = list()
    abvAveNums = list()

    for num in nums:
        if num < aveNum:
            blwAveNums.append(num)
        elif num == aveNum:
            aveNums.append(num)
        else:
            abvAveNums.append(num)

    print(f"Below average values: {blwAveNums}")

    if len(aveNums) > 0:
        print(f"Average values: {aveNums}")

    print(f"Above average values: {abvAveNums}")
except ZeroDivisionError:
    print("HAH! Did you think we did not think of that? NO! No seriously, our answer is no!")