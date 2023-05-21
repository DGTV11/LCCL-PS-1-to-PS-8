# DANIEL LAZY CAME-TO-MY-MIND-FIRST METHOD

def isSublist(larger, smaller):
    if smaller == list():
        return True

    l = str()
    s = str()
    
    
    for item in larger:
        if type(item) == str:
            l += f'"{item}"'
        elif type(item) in [int, float]:
            l += f'{item}'
        elif type(item) in [list, tuple]:
            l += f'{str(item)}'
        elif type(item) == range:
            l += f'{str(list(item))}'
    for item in smaller:
        if type(item) == str:
            s += f'"{item}"'
        elif type(item) in [int, float]:
            s += f'{item}'
        elif type(item) in [list, tuple]:
            s += f'{str(item)}'
        elif type(item) == range:
            s += f'{str(list(item))}'
    if l.replace(s, str()) != l:
        return True
    else:
        return False

if __name__ == '__main__':
    print(isSublist([1, 312312, 12], []))
    print(isSublist([1122, 312321, 21, "1qw1`", [23798]], [21, "1qw1`", [23798]]))