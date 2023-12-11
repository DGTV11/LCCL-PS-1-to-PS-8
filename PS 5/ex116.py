from ex115 import pDivs

def isPerf(n):
    n = int(n)
    d = pDivs(n)
    return (sum(d)-n) == n

if __name__ == '__main__':
    for i in range(1, 10001):
        # i = 28
        if isPerf(i):
            print(i)