import emoji


def main():
    i = input("Input: ")
    print(f"Output: {emojizar(i)}")


def emojizar(prompt):
    return emoji.emojize(prompt, language="alias")


main()
