OPS = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
    "^": 3
}

def precedence(operator):
    if not (operator in OPS.keys()):
        raise ValueError("The input is not an operator!")
    else:
        return OPS[operator]

if __name__ == "__main__":
    p = precedence(input("Please input an operator: "))
    print(f"The inputted operator has a precedence of {p}")