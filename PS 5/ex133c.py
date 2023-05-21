# METHOD OF PURE AGONYs

def isSublist(larger, smaller):
    x = 0
    while x <= len(larger)-1:
        x = 0
        if smaller == larger[x:len(smaller)+x-1]:
            return True
        x += 1
    return False

if __name__ == '__main__':
    print(isSublist([1, 312312, 12], []))
    print(isSublist([1122, 312321, 21, "1qw1`", [23798]], [21, "1qw1`", [23798]]))