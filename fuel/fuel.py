## input x/y





while True:
    try:
        tank = input("Fraction: ").split("/")
        x = int(tank[0])
        y = int(tank[1])
    except ValueError:
        break
    except ZeroDivisionError:
        break
    



