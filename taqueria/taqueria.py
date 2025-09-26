import string

taqueria = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    pedido = []
    while True:
        try:
            item = input("Item: ")
            item = formatar_item(item)
            pedido.append(taqueria[item])
            exibir_total(pedido)
        except EOFError:
            break
        except KeyError:
            pass


def formatar_item(item : str) -> str:

## capwords - separa string com split - usa capitalize e da join. Sep = ' ' por padrão.
    return string.capwords(item, sep=' ').strip()


def exibir_total(pedido: list[float]) -> None:
    total = sum(pedido)
    print(f"Total: ${total:.2f}")


main()
