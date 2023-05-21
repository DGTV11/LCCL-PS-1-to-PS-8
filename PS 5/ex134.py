def allSubLists(_list):
    l = len(_list)
    s = [[]]
    sx = list()
    for i in range(0, l):
        lastindex = i
        while lastindex != l:
            sx = _list[lastindex-i:lastindex+1]
            if sx not in s:
                s.append(sx)
            lastindex += 1
    return s

if __name__ == '__main__':
    print(allSubLists([1, 2, 3]))
    print(allSubLists([1, 2, 3, 4]))
    print(allSubLists([1, 2, 3, 4, 5]))
    print(allSubLists([1, 1, 1]))