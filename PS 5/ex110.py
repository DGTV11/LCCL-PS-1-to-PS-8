nums = list()
while True:
    x = int(input("Please input an integer (all floats will be integerised, type 0 to quit): "))

    if x == 0:
        break
    else:
        nums.append(x)

for item in sorted(nums):
    print(item)