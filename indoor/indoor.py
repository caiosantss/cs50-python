def main():
    word = input("Write a phrase: ")
    print(lowerCase(word))


def lowerCase(word):
   return word.casefold()

main()
