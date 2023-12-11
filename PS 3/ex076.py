'''
Initialize factor to two
While factor is less than or equal to n do
    If n is evenly divisible by factor then 
        Conclude that factor is a factor of n 
        Divide n by factor using integer division
    Else
        Increase factor by one
'''

n = int(input('Enter an integer (2 or greater): '))

if n < 2:
    raise ValueError('ERROR: Variable n must be more than or equal to 2!')

print(f"The prime factors of {n} are:")

f = 2
while f <= n:
    if n % f == 0:
        print(f)
        n //= f
    else:
        f += 1