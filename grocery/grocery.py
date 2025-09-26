def main():

    items = {}
    while True:
        try:
            item = input()
            items[item] = items.get(item, 0) + 1
        except EOFError:
            return formata_dicionario(items)

def formata_dicionario(dicionario_items : dict) -> None:
    for key_item, valor_item in sorted(dicionario_items.items()):
        print(valor_item, key_item.upper())

main()



