import random


def main():
    n = get_level()
    score = play_game(n)
    print(f"Score: {score}")


def get_level():
    # Mantem um Loop infinito se o level não for valido
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except:
            pass


#Gerar inteiro conforme o nivel - utilizando biblioteca random
def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)



# Jogo
def play_game(level):
    score = 0

    for i in range(10):
        tentativas = 1

        x = generate_integer(level)
        y = generate_integer(level)

        ## Validando tentativas do usuario e tratando tentativas erradas
        while tentativas <= 3:
            try:
                resposta = int(input(f"{x} + {y} = "))
                if resposta == x + y:
                    score += 1
                    break
                else:
                    tentativas += 1
                    print("EEE")
            except:
                tentativas += 1
                print("EEE")

        if tentativas > 3:
            print(f"{x} + {y} = {x + y}")

    return score


if __name__ == "__main__":
    main()
