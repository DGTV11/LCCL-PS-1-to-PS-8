# DANIEL EVEN MORE LAZY METHOD

import ex134
def isSublist(larger: list, smaller: list) -> bool:
     return smaller in ex134.allSubLists(larger)

if __name__ == '__main__':
    print(isSublist([1, 312312, 12], []))
    print(isSublist([1122, 312321, 21, "1qw1`", [23798]], [21, "1qw1`", [23798]]))