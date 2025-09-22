def main():
    show_tank = tank()
    print(show_tank)




def tank():
    while True:
        try:
            tank = input("Fraction: ").split("/")
            x = convert_int(tank[0])
            y = convert_int(tank[1])
            if x <= y and x >= 0:
                return show_percentage(x, y)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


def convert_int(n):
    return int(n)


def show_percentage(n1, n2):
    porcentagem = int((n1 / n2) * 100)
    if porcentagem <= 1:
        return "E"
    elif porcentagem >= 99:
        return "F"
    else:
        return f"{porcentagem}%"



main()


