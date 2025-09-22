def main():
    show_tank = tank()
    print(show_tank)




def tank():
    while True:
        try:
            tank = input("Fraction: ").split("/")
            x = convert_int(tank[0])
            y = convert_int(tank[1])
            return show_percentage(x, y)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


def convert_int(n):
    try:
        if n.isnum() and n > 0:
            return int(n)
    except ValueError:
        print("The value must be a number")


def show_percentage(n1, n2):
    return int((n1 / n2) * 100)


main()


