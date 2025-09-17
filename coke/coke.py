## Amont due: how much must be paid yet
## Input a coin: Coin value : 25, 10, 5 - only integer.
## amont Due -- Loop until

def main():
    coke_price = 50
    total_inserted = 0

    while total_inserted < coke_price:
        print(f"Amount Due: {coke_price - total_inserted}")
        coin = input("Insert Coin: ")

        if is_coin(coin):
            total_inserted += coin_to_int(coin)
        else:
            # moeda inválida, só ignora
            continue

    print(f"Change Owed: {total_inserted - coke_price}")


def is_coin(coin):
    return coin in ("25", "10", "5")

def coin_to_int(coin):
    return int(coin)


main()




