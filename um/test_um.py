import pytest
from um import count

def test_correct_count():
    assert count("Um, I think um we should um go.") == 3
    assert count("This is a test.") == 0
    assert count("Um... um... um...") == 3
    assert count("UM, um, Um!") == 3
    assert count("Summary of the album.") == 0
    assert count("Um, I am not sure if um this is correct.") == 2

def test_incorrect_count():
    assert count("Um, I think um we should um go.") != 2
    assert count("This is a test.") != 1
    assert count("Um... um... um...") != 4
    assert count("UM, um, Um!") != 0

def test_edge_cases():
    assert count("") == 0
    assert count("um") == 1
    assert count("UM") == 1
    assert count("uM") == 1
    assert count("Um um um um um") == 5
    assert count("Um, um, um, um, um.") == 5


