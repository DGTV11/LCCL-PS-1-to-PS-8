'''
If you have 3 straws, possibly of differing lengths, it may or may not 
be possible to lay them down so that they form a triangle when their 
ends are touching. For example, if all of the straws have a length of 6 
inches then one can easily construct an equilateral triangle using them. 
However, if one straw is 6 inches long, while the other two are each 
only 2 inches long, then a triangle cannot be formed. More generally, if 
any one length is greater than or equal to the sum of the other two then
the lengths cannot be used to form a triangle. Otherwise they can form a 
triangle. Write a function that determines whether or not three lengths 
can form a triangle. The function will take 3 parameters and return a 
Boolean result. If any of the lengths are less than or equal to 0 then 
your function should return False. Otherwise it should determine whether 
or not the lengths can be used to form a triangle using the method 
described in the previous paragraph, and return the appropriate result. 
In addition, write a program that reads 3 lengths from the user and 
demonstrates the behaviour of your function.
'''

def Triangle(a, b, c):
    c0 = not ((a == 0) or (b == 0) or (c == 0))
    
    maxy = max(a, b, c)
    c1 = not (maxy >= ((a + b + c) - maxy))

    if c0 and c1:
        return True
    else:
        return False
    
if __name__ == '__main__':
    out = Triangle(float(input('Length 1: ')), float(input('Length 2: ')), float(input('Length 3: ')))

    if out:
        print('Lengths can make a triangle!')
    else:
        print('Lengths cannot make a triangle!')