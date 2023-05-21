from random import randint, choice
import string
def randLicencePlate():
    plate = str()
    for i in range(randint(3, 4)):
        plate += choice(string.digits)
    for i in range(3):
        plate += choice(string.ascii_letters)
    return plate

if __name__ == "__main__":
    print(f"Generated licence plate: {randLicencePlate()}")