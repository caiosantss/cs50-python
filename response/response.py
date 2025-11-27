from validator_collection import validators, checkers, errors


def main():
    email = input("Email: ")
    ok, email = validar_email(email)
    if ok:
        print("Valid")
    else:
        print(f"Invalid")

def validar_email(email):

    try:
        email_valido = validators.email(email, allow_empty=False)
        return True, email_valido
    except errors.InvalidEmailError as e:
        return False, e
    except errors.EmptyValueError as e:
        return False, e






main()


