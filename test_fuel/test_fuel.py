from fuel import convert, gauge
import pytest

# Test convert with exception ValueError:
def test_convert_error():

    # Y não pode ser 0
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

    # len(fração) > 2
    with pytest.raises(ValueError):
        convert("1/2/3")

    # x > y
    with pytest.raises(ValueError):
        convert("5/2")

    # not a number
    with pytest.raises(ValueError):
        convert("b/A")

    # not positive numbers
    with pytest.raises(ValueError):
        convert("-1/3")


def test_convert():
    assert convert("1/2") == 50
    assert convert("1/100") == 1


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"

    for numero in range(2, 99):
        assert gauge(numero) == f"{numero}%"
