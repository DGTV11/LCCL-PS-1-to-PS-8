def isInteger(_str):
    s = (_str.strip()).lstrip("-")
    return s.isdigit()

if __name__ == "__main__":
    if isInteger(input("Please input something (numbers are preferred): ")):
        print("Input represents an integer!")
    else:
        print("Input does not represent an integer!")