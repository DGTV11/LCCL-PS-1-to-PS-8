from string import ascii_letters

def tokenise(str_):
    filtd_1 = str_.strip().split()
    filtd_2 = list()
    for blob in filtd_1:
        for iu, c in enumerate(blob):
            if c in ascii_letters:
                iux = iu
                break
        for id, c in tuple(enumerate(blob))[::-1]:
            if c in ascii_letters:
                idx = id + 1
                break

        try:
            filtd_2.append(blob[iux:idx])
        except IndexError:
            continue

    return filtd_2

print(tokenise(input('Please input text: ')))