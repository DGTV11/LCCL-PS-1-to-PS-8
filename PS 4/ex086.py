BASE_FARE = 4.00
ADDITIONAL_COSTS = 0.25

def calculate(dist, precise=False):
    m = dist * 1000
    if precise:
        cost = BASE_FARE + ((m/140) * ADDITIONAL_COSTS)
    else:
        cost = BASE_FARE + ((m//140) * ADDITIONAL_COSTS)
    
    return cost

if __name__ == "__main__":
    print("Fare: $%f"%calculate(float(input("Distance in km? "))))