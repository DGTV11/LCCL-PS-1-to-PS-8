class nullItem:
    def __init__(self, idx):
        self.idx = idx
    def __repr__(self):
        return f'nullItem with index {self.idx}'

n = nullItem(0)
print(type(n) is nullItem)

def isSublist(l, sl):
    lx = l

    for i, item in enumerate(l):
        if item in sl:
            for o, e in enumerate(sl):
                if item == e:
                    lx[i] = nullItem(o)
                    break

    slr = list(range(len(sl)))
    print("slr:", slr)
    eee = []
    ee = []
    print("lx:", lx)
    for item in lx:
        if type(item) is nullItem:
            ee.append(item.idx)
        else:
            eee.append(ee)
            ee = []
    print("eee:", eee)
    return slr in eee

if __name__ == '__main__':
    print(isSublist([1, 312312, 12], []))
    print(isSublist([1122, 312321, 21, "1qw1`", [23798]], [21, "1qw1`", [23798]]))