def centerStr(s, w):
    if len(s) >= w:
        return s
    else:
        spaces = abs((len(s) - w) // 2) * " "
        return spaces + s

if __name__ == '__main__':
    print(centerStr("Hello, world!", 25))
    print(centerStr("EEEEEEEEEEEEEEE", 25))
    print(centerStr("EEEEEEEEEEEEEEEEEEEEEEEEE", 25))