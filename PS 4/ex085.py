def sqr(n):
    return n**2

def sqrt(n):
    guess = n / 2

    while abs((sqr(guess)) - n) >= 10**(-12):
        guess = (guess + (n/guess)) / 2

    return guess

def hyp(base, height):
    #a^2+b^2=c^2
    c2 = sqr(base) + sqr(height)
    return sqrt(c2)

if __name__ == "__main__":
    b = float(input("Base of right triangle? "))
    h = float(input("Height of right triangle? "))
    print(f"The hypotenuse of the inputed right triangle is {hyp(b, h)}.")