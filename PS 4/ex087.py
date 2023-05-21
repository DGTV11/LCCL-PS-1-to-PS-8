BASE_COST = 10.95
ADDITIONAL_COSTS = 2.95

def calculate(n):
    cost = BASE_COST + ((n-1) * ADDITIONAL_COSTS)
    return cost

if __name__ == "__main__":
    print("Cost: $%s"%calculate(float(input("Number of items? "))))