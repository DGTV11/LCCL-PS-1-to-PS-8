def reverseLookup(_dict, value):
    keys = list()
    for k, v in _dict.items():
        if v == value:
            keys.append(k)
    return keys

if __name__ == '__main__':
    x = {'13321': '213', '213123': '123312', '1233312': '213', '132312312213': '213'}
    print(reverseLookup(x, '213'))
    print(reverseLookup(x, '123312'))
    print(reverseLookup(x, '12345'))