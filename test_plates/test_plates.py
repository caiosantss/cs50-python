from plates import is_valid

def test_max_min_charaters():
    assert is_valid("HELLOooooo") == False
    assert is_valid("Hello") == True


def test_is_number_end():
    ## Have a number at the end
    assert is_valid("CS50P") == False


def test_is_alphanumeric():
    ## is not alhpanumeric
    assert is_valid("CS.50") == False
    ## is alhpanumeric
    assert is_valid("CS50") == True


def test_is_first_number_zero():
    # First Number cannot be 0
    assert is_valid("AB9512") == True
    assert is_valid("LP018") == False

def test_start_two_letters():
    #All vanity plates must start with at least two letters.
    assert is_valid("55") == False
    assert is_valid("LL55") == True
