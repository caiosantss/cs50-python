def main():
    ...


def value(greeting):

    greetingTratada = greeting.strip().lower()

    ## tem hello e qualquer outra coisa -> 0
    if greetingTratada.find("hello") == 0:
        return 0

    ## começa com h e não é hello -> 20
    elif greetingTratada.startswith("h"):
        return 20

    ## é qualquer outra coisa
    else:
        return 100


if __name__ == "__main__":
    main()

