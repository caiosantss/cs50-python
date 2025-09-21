## input x/y





while True:
    try:
        tank = input("Fraction: ").split("/")
        x = convert_int(x)
        y = convert_int(y)
        return x / y
    except ValueError:
        break
    except ZeroDivisionError:
        break


def convert_int(n):
    try:
        return int(n)
    except ValueError:
        print("The value must be a number")



##If, though, X or Y is not an integer, X is greater than Y, or Y is 0
