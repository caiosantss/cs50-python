import random

def main():
    # n = int > 0 / reprompt
    while True:
        n = input("Level: ")
        if not n.isdecimal():
            continue

        n = int(n)
        if n > 0:
            break

    guess_system = random.randint(1, n)

    while True:
        # Guess = int > 0 / reprompt: numero random gerado entre 1 e n
        guess_user = input("Guess: ")

        if not guess_user.isdecimal():
            continue

        guess_user = int(guess_user)

        if guess_user <= 0:
            continue

        # guess < numero random : Too small!, > Too large!, = Just right!
        if guess_output(guess_system, guess_user):
            break


def guess_output(guess_system: int, guess_user: int):
    if guess_system < guess_user:
        print("Too large!")
    elif guess_system > guess_user:
        print("Too small!")
    else:
        print("Just right!")
        return True
    return False


main()
