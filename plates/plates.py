def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):

    if start_two_letters(plate):
        print("1 start_two_letters") ## ok
    if max_min_charaters(plate):
        print("2 max_min_charaters(plate)") ## ok
    if is_number_end(plate):
        print("3 is_number_end(plate)") ## ok
    if is_first_number_zero(plate):
        print("4 is_firtsnumber_zero") ## NOT OK
    if is_alphanumerico(plate):
        print("5 is_alphanumerico") ## ok

"""
OK - 1 - All vanity plates must start with at least two letters.
OK - 2 - vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
OK - 3 - Numbers cannot be used in the middle of a plate they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
OK - 4 - The first number used cannot be a 0.
OK - 5 - No periods, spaces, or punctuation marks are allowed.
"""

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
def is_number_end(plate):
    find_number = False
    for i in plate:
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
            if numero == '0':
                contador += 1
                return False
            else:
                return True


 ## 5 No periods, spaces, or punctuation marks are allowed:
def is_alphanumerico(palavra):
   return palavra.isalnum()
##is alphanumeric - only letters and numbers


main()






