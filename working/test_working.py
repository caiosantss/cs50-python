import pytest
from working import convert


def test_valid_inputs():
    # Casos válidos
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("11:59 PM to 12:01 AM") == "23:59 to 00:01"


def test_invalid_inputs():
    # Casos inválidos — devem levantar ValueError
    invalid_cases = [
        "9:60 AM to 5:60 PM",
        "9 AM - 5 PM",         
        "09:00 AM - 17:00 PM",
        "25 AM to 5 PM",
        "9:00 to 5:00",
        "9 AM to 13 PM",
        "9AM to5PM",
        "10:30 XM to 8 AM"
    ]

    for case in invalid_cases:
        with pytest.raises(ValueError):
            convert(case)


def test_edge_cases():
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"  # meio-dia até meia-noite
    assert convert("1:05 AM to 1:05 PM") == "01:05 to 13:05"  # mesmo minuto, AM → PM
