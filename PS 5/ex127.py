from inputs import inpList

def isSorted(l):
    return l == sorted(l)

if __name__ == '__main__':
    l = inpList("Pick a float, any float (type nothing and enter to quit): ", "float", "")
    print(isSorted(l))