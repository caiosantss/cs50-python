def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    return all(
        [
            start_two_letters(plate),
            max_min_charaters(plate),
            is_number_end(plate),
            is_first_number_zero(plate),
            is_alphanumerico(plate),
        ]
    )


## 1 - All vanity plates must start with at least two letters.
def start_two_letters(palavra):
    return palavra[0:2].isalpha()


## 2 -Return True if its between 2 and 6
def max_min_charaters(palavra):
    if len(palavra) >= 2 and len(palavra) <= 6:
        return True
    else:
        return False


## 3 Numbers cannot be used in the middle of a plate
def is_number_end(palavra):
    find_number = False
    for i in palavra:
        if i.isdigit():
            find_number = True
        elif find_number and i.isalpha():
            return False
    return True


## 4 First number cannot be 0
def is_first_number_zero(palavra):
    contador = 0
    for numero in palavra:
        if numero.isdecimal() and contador == 0:
            if numero == "0":
                contador += 1
                return False
            else:
                return True
        elif palavra.isalpha():
            return True


## 5 No periods, spaces, or punctuation marks are allowed:
def is_alphanumerico(palavra):
    return palavra.isalnum()


if __name__ == "__main__":
    main()
