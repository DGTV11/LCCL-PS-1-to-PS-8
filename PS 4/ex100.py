from random import randint
def randPW(big=False):
    '''
    big=False -> returns a random password from 7 to 10 chars long
    big=True -> returns a random password from 20 to 25 chars long
    '''
    pw = str()
    if not big:
        _len = randint(7, 10)
    else:
        _len = randint(20, 25)
    for i in range(_len):
        pw += chr(randint(33, 126))
    return pw

if __name__ == "__main__":
    if input("Long password or short password (l/s)? : ") in ["l", "L"]:
        x = True
    else:
        x = False
    print(f"Generated password: {randPW(big=x)}")