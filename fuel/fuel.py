def main():
    show_tank = tank()
    print(show_tank)

def tank():
    while True:
        try:
            fraction = input("Fraction: ")
            x = int(parts[0])
            y = int(parts[1])
            if x <= y and x >= 0:
                return show_percentage(x, y)
        except (ValueError, ZeroDivisionError):
            pass


def valid_fraction(fraction):
    parts = fraction.split("/")
        if len(parts) != 2:



def show_percentage(n1, n2):
        porcentagem = round((n1 / n2) * 100)
        if porcentagem <= 1:
            return "E"
        elif porcentagem >= 99:
            return "F"
        else:
            return f"{porcentagem}%"

main()


