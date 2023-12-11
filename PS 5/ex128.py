import random

def countRange(l, _min, _max):
    ddd = int()
    for item in l:
        if _max > item >= _min:
            ddd += 1
    return ddd

if __name__ == '__main__':
    for i in range(1, 15):
        eee = list()
        _len = random.randint(5, 100)
        for i in range(_len):
            eee.append(random.random()*50)
        mn = random.randint(0, _len//2)
        mx = random.randint(mn+1, _len)
        print(f"List: {eee}\nMin value: {mn}\nMax value: {mx}\nOutput: {countRange(eee, mn, mx)}")