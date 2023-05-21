def trim_data(data, n):
    s_data = sorted(data)
    for i in range(n):
        s_data.pop()
        s_data.reverse()
        s_data.pop()
        s_data.reverse()
    return s_data

if __name__ == "__main__":
    d = input("Input all numbers from a dataset (split by adding spaces): ").split()
    n = int(input("Number of numbers from each extreme to trim: "))

    dd = list()
    for item in d:
        dd.append(float(item))

    ddd = sorted(dd)

    if len(d) < 4:
        raise IndexError("Dataset is too short!")

    print(f"TRIMMED DATASET: {trim_data(ddd, n)}")
    print(f"ORIGINAL DATASET: {ddd}")