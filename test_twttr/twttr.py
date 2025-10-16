def main():

    user_input = input("Input: ")
    print(shorten(user_input))

##pegar palavra - tirar todas as vogais
def shorten(word: str) -> str:

    new_word = ""

    for letter in word:
        if letter.lower() not in ("a", "e", "i", "o", "u"):
            new_word += letter
    return new_word


if __name__ == "__main__":
    main()
