'''
Read x from the user
Initialize guess to x /2
While guess is not good enough do
    Update guess to be the average of guess and x /guess

In the author's solution, guess was considered good enough when the absolute value
of the difference between guess * guess and x was less than or equal to 10 ** (-12).
'''

def approx_sqrt(input_float: float, guess: float=1.0) -> float:
    if abs((guess**2) - input_float) < 1e-12:
        return guess
    
    return approx_sqrt(input_float, (guess+(input_float/guess))/2)


if __name__ == '__main__':
    input_float = float(input('Input number: '))
    inital_guess = 1.0 if input('Inital guess? (1 for 1, else input/2): ') == '1' else input_float/2
    print(f'The square root of {input_float} is approximately {approx_sqrt(input_float, inital_guess)}.')