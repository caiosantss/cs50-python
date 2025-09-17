def main():
    palavra = input("Palavra: ")
    print(camel_to_snake(palavra))

def camel_to_snake(input):

    texto_camel_case = ""

    for index, letra in enumerate(input):
        if letra.isupper() and index != 0:
           texto_camel_case += f"_{letra.lower()}"
        else:
            texto_camel_case += letra.lower()

    return texto_camel_case


main()
