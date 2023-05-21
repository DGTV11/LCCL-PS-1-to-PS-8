import string, re

def isPWgood(pw=str()):
    return any(ele.isupper() for ele in pw) and any(ele.islower() for ele in pw) and any(ele.isnumeric() for ele in pw) and (len(pw) >= 8)

if __name__ == "__main__":
    _in = input("Password: ")
    if isPWgood(_in):
        print(f"The password {_in} is a good password")
    else:
        print(f"The password {_in} is a bad password")