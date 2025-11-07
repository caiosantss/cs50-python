from numb3rs import validate
import pytest


def test_is_ipv4():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True

def test_isnot_ipv4():
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("192.168.001.1") == False
    assert validate("cat") == False



