import pytest
from seasons import convert_input_date, diference_in_minutes, number_to_words, get_date_now

def test_convert_input_date():
    date_correct = "2023-12-02"
    expected_date = (convert_input_date(date_correct))
    assert expected_date.year == 2023
    assert expected_date.month == 12
    assert expected_date.day == 2

    # Test invalid formats
    with pytest.raises(ValueError):
        convert_input_date("2023/12/02")
        convert_input_date("12-02-2023")
        convert_input_date("blabla")

def test_diference_in_minutes():
    # One day difference
    assert diference_in_minutes(convert_input_date("2023-12-01"), convert_input_date("2023-12-02")) == pytest.approx(1440)

    # Leap year test
    assert diference_in_minutes(convert_input_date("2023-01-01"), convert_input_date("2025-01-01")) == pytest.approx(1052640)


def test_number_to_words():
    assert number_to_words(0) == "Zero"
    assert number_to_words(1) == "One"
    assert number_to_words(12) == "Twelve"
    assert number_to_words(25) == "Twenty-five"
    assert number_to_words(100) == "One hundred"
    assert number_to_words(1234) == "One thousand, two hundred thirty-four"
