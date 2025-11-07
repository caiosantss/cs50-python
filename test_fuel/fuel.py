def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    # Divide a string em X e Y
    parts = fraction.split("/")
    if len(parts) != 2:
        raise ValueError

    try:
        x = int(parts[0])
        y = int(parts[1])
    except ValueError:
        raise ValueError

    # Nao poder ser divizivel por 0 - error
    if y == 0:
        raise ZeroDivisionError

    if x > y or x < 0:
        raise ValueError

    # Calcula o percentual arredondado
    percentage = round((x / y) * 100)

    # Garante que o valor fique entre 0 e 100
    if percentage < 0:
        percentage = 0
    elif percentage > 100:
        percentage = 100

    return percentage


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
