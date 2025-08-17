def get_guess():
    guess = input("Enter a guess: ")
    return guess


def main():
    gess = get_guess()
    if guess == 50:
        print("Correct")
    else:
        print("Incorrect")


main()
