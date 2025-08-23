def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Deve aceitar uma str como input, formatada como $##.##, cada # é um digito decimal. REMOVA O $ e retorne o float. EX: $50.00 > 50.0
    d = d.replace("$", "")
    d = float(d)
    return d



def percent_to_float(p):
    # Recebe uma str ##%, remova % e retorne a porcentagem como float. EX: 15% > 0.15

    p = p.replace("%", "")
    p = float(p)
    p = p / 100.0
    return p


main()
