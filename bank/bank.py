"""
- Se receber "Hello, e qualquer outra coisa"  como input -> $0 como output
    -Método se contém palavra dentro de uma string, com tratamento de espaços.

- Se receber alguma coisa com H, que não seja Hello -> output $20
    -Método se inicia com uma letra, talvez usar indice pois string é um array

- Qualquer outro caso -> $100
    else?

- Ignorar qualquer espaço em branco e tratar case-insensitively
    - Tratamento
"""

def tratamento_string(s:str):
   return s.strip().lower()


def output_greeting(greeting) -> str:

    greetingTratada = tratamento_string(greeting)

    ## tem hello e qualquer outra coisa -> 0
    if greetingTratada.find("hello") == 0:
        return "$0"

    ## começa com h e não é hello -> 20
    elif greetingTratada.startswith("h"):
        return "$20"

    ## é qualquer outra coisa
    else:
        return "$100"


def main():
    greeting = str(input("Greeting: "))
    print((output_greeting(greeting)))


main()


