from math import sqrt
def isPrime(_int):
    n = int(_int)
    nx = n
    factors = []
    while True:
        if (n % nx) == 0:
            factors.append(nx)
        nx -= 1
        if nx == round(sqrt(n)):
            break
    return ((len(factors) > 1) and (len(factors) < 3))

if __name__ == "__main__":
    i = input("Input an integer: ")
    x = isPrime(i)
    
    if x:
        print(f"The integer {int(i)} is a prime number!")
    else:
        print(f"The integer {int(i)} is not a prime number!")