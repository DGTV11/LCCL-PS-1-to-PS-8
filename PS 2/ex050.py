'''
A univariate quadratic function has the form 
f(x) = (ax**2) + bx + c, where a, b and c are constants, 
and a is non-zero. The roots of a quadratic function can 
be found by finding the values of x that satisfy the 
quadratic equation ax2 + bx + c = 0. A quadratic function 
may have 0, 1 or 2 real roots. These roots can be 
computed using the quadratic formula, shown below:

root = -b ± root((b**2) - 4ac)
       -----------------------
                 2a

The portion of the expression under the square root sign is called the discriminant.
If the discriminant is negative then the quadratic equation does not have any real roots. If the discriminant is 0, then the equation has one real root. Otherwise the equation has two real roots, and the expression must be evaluated twice, once using a plus sign, and once using a minus sign, when computing the numerator.
Write a program that computes the real roots of a quadratic function. Your program should begin by prompting the user for the values of a, b and c. Then it should display a message indicating the number of real roots, along with the values of the real roots (if any).
'''
try:
    import math

    a = abs(int(input('Input quadratic value a (Will be absoluted): ')))
    b = int(input('Input quadratic value b: '))
    c = int(input('Input quadratic value c: '))

    root2 = None
    disc = (b**2) - (4*(a*c))
    if disc < 0:
        raise ValueError('No real roots!')
    elif disc == 0:
        print('1 real root!')
    else:
        root2 = True
        print('2 real roots!')

    print(f'x (Root 1) = {float( ( (-b) + math.sqrt(disc) )/(2*a) )}')

    if root2:
        print(f'x (Root 2) = {float( ( (-b) - math.sqrt(disc) )/(2*a) )}')

except Exception as e:
    print(e)