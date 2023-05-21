'''
In a particular jurisdiction, older license 
plates consist of three uppercase letters 
followed by three numbers. When all of the 
license plates following that pattern had been 
used, the format was changed to four numbers 
followed by three uppercase letters. Write a 
program that begins by reading a string of 
characters from the user. Then your program 
should display a message indicating whether the 
characters are valid for an older style license 
plate or a newer style license plate. Your 
program should display an appropriate message if 
the string entered by the user is not valid for 
either style of license plate.
'''

plate = input('Licence Plate: ')

if plate[0:2].isupper() and plate[3:5].isdigit():
    print('The plate number is valid for an older style license')
elif plate[0:3].isdigit() and plate[4:6].isupper():
    print('The plate number is valid for an newer style license')
else:
    print('The plate number is not valid for either style of license plate.')