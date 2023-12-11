from ex098 import *

def nextPrime(_int):
    n = int(_int)
    nx = n+1
    while True:
        if isPrime(nx):
            break
        nx += 1
    return nx

if __name__ == "__main__":
    i = input("Input an integer: ")
    x = nextPrime(i)
    
    print(f"The next prime after the integer {int(i)} is {x}")