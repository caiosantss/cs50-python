def main():

    user_input = input("Input: ")
    print(remove_vowel(user_input))

##pegar palavra - tirar todas as vogais

def is_vowel(letra):
    if letra in ("A", "E", "I", "O", "U") or  letra in ("a", "e", "i", "o", "u"):
        return True
    else:
        return False

def remove_vowel(word):
    new_word = ""
    for letter in word:
        if is_vowel(letter):
             word.replace(letter, "")
        else:
            new_word += letter
    return new_word


main()
