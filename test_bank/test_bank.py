from bank import value


def test_return_value():
    assert value("HelLo") == 0
    assert value("hEy") == 20
    assert value("Something Else") == 100




