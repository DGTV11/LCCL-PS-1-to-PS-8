def trim_data(data, n):
    return sorted(data)[n:-n]

if __name__ == "__main__":
    d = input("Input all numbers from a dataset (split by adding spaces): ").split()
    n = int(input("Number of numbers from each extreme to trim: "))

    # dd = list()
    # for item in d:
    #     dd.append(float(item))

    dd = map(float, d)

    ddd = sorted(dd)

    if len(d) < 4:
        raise IndexError("Dataset is too short!")

    print(f"TRIMMED DATASET: {trim_data(ddd, n)}")
    print(f"ORIGINAL DATASET: {ddd}")