#CANNOT USE LOOPS == CANNOT USE INPUTS MODULE

def add_input_num(num=0.0):
    x = input("Input number (press enter to exit): ")
    if x == '':
        return num
    return add_input_num(num+float(x))

if __name__ == '__main__':
    print(f'Total: {add_input_num()}')