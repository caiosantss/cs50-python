import inflect


p = inflect.engine()
nomes = []
prefixo = "Adieu, adieu, to "


while True:
    try:
        nome = str(input("Nome: "))
        if nome != "":
            nomes.append(nome)
    except EOFError:
        print()
        break


print(prefixo + p.join((nomes)))



