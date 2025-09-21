## input x/y




def tank():
    while True:
        try:
            tank = input("Fraction: ").split("/")
            x = convert_int(x)
            y = convert_int(y)
            return 
        except ValueError:
            print("The value must be a number")
        except ZeroDivisionError:
            print("The value must be bigger than 0")

def convert_int(n):
    try:
        if n.isnum() and n > 0
        return int(n)
    except ValueError:
        print("The value must be a number")

