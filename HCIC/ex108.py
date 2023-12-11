def divWhRemainder(dividend, divisor):
    quotent = dividend // divisor 
    remainder = dividend % divisor
    return quotent, remainder

'''
One cup is equivalent to 16 tablespoons. 
One tablespoon is equivalent to 3 teaspoons.
'''

def reduce(val, type):
    if type == 3: # cups
        return f'0 teaspoons, 0 tablespoons, {val} cups'
    elif type == 2: # tablespoons
        x, y = divWhRemainder(val, 16)
        return f'0 teaspoons, {y} tablespoons, {x} cups'
    elif type == 1: # teaspoons
        x, y = divWhRemainder(val, 3)
        z, x = divWhRemainder(x, 16)
        return f'{y} teaspoons, {x} tablespoons, {z} cups'

if __name__ == '__main__':
    val = int(input('Number of units: '))
    type = int(input('Type of units (1 for teaspoons, 2 for tablespoons, 3 for cups): '))

    print(reduce(reduce(val, type)))