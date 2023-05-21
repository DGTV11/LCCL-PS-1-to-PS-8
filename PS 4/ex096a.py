def isInteger(_str):
    try:
        int(_str)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    if isInteger(input("Please input something (numbers are preferred): ")):
        print("Input represents an integer!")
    else:
        print("Input does not represent an integer!")