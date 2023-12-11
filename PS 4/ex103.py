import ex100, ex102

def main(b=False):
    '''
    b=False -> returns a random good password from 7 to 10 chars long
    b=True -> returns a random good password from 20 to 25 chars long
    '''
    i = 1
    while True:
        x = ex100.randPW(big=b)
        if ex102.isPWgood(x):
            break
        else:
            i += 1
    return x, i

if __name__ == "__main__":
    if input("Long good password or short good password (l/s)? : ") in ["l", "L"]:
        xx = True
    else:
        xx = False
    out = main(b=xx)
    print(f"Generated good password ({out[1]} attempts): {out[0]}")