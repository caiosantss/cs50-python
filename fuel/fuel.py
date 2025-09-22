def main():

while True:
    tank = input("Fraction: ").split("/")
    l = show_tank(tank)
    print(l)




def show_tank(fraction):
        try:
            x = convert_int(fraction[0])
            y = convert_int(fraction[1])
            return show_percentage(x, y)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


def convert_int(n):
    try:
        if n.isnum() and n > 0
        return int(n)
    except ValueError:
        print("The value must be a number")


def show_percentage(n1, n2):
    return porcentage = int((n1 / n2) * 100)

main()


