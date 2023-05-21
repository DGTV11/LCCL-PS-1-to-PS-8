print("    1   2   3   4   5   6   7   8   9   10")

for i in range(1, 11):
    if i >= 10:
        print(i, end="  ")
    else:
        print(i, end="   ")

    for x in range(1, 11):
        num = x * i
        if num >= 10:
            print(x * i, end="  ")
        else:
            print(x * i, end="   ")
    print()