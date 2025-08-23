def Main():
    mass = input("Type Mass in Kg: ")
    int(mass)
    energy = energyFormulaCalculate(mass)
    print(int(energy))


def energyFormulaCalculate(mass):
    SpeedOfLight = 300000000
    energy = int(mass) * pow(SpeedOfLight, 2)
    return energy

Main()

