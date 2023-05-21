'''
Read x from the user
Initialize guess to x /2
While guess is not good enough do
    Update guess to be the average of guess and x /guess

In the author's solution, guess was considered good enough when the absolute value
of the difference between guess * guess and x was less than or equal to 10 ** (-12).
'''

i = False
x = float(input('Input number: '))
if x < 0:
    x = abs(x)
    i = True

guess = x / 2

while abs((guess**2) - x) >= 10**(-12):
    guess = (guess + (x/guess)) / 2

if i:
    print(f'The square root of {x} is approximately {guess}i.')
else:
    print(f'The square root of {x} is approximately {guess}.')