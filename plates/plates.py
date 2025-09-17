def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

"""
1 - All vanity plates must start with at least two letters.
OK - 2 - vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
3 - Numbers cannot be used in the middle of a plate they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
OK - 4 - The first number used cannot be a 0.
OK - 5 - No periods, spaces, or punctuation marks are allowed.

"""

def max_min_charaters(palavra):
    """ vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters """

    contador = 0
    for letra in palavra:
        contador += 1
    if contador >= 2 and contador <= 6:
        return True
    else:
        Return False


def start(palavra):
    palavra.

def is_alphanumerico(palavra):
   return palavra.isalnum()

    """“No periods, spaces, or punctuation marks are allowed.”"""


def is_first_number_zero(palavra):
    contador = 0
    for numero in palavra:
        if numero.isdecimal() and contador == 0:
            if numero == '0':
                contador += 1
                return True
            else:
                contador += 1
                return False


