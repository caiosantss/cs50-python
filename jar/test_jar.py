from jar import Jar
import pytest


def test_init():
    jar = Jar()
    asssert jat.capacity == 12
    assert jar.size == 0

    # negative capacity

    with pytest.raises(ValueError):
        Jar(-1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(7)
    assert jar.size == 12

    # n < 0
    with pytest.raises(ValueError):
        jar.deposit(-1)

    # exceed capacity
    with pytest.raises(ValueError):
        jar.deposit(1)


def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2
    jar.withdraw(2)
    assert jar.size == 0

    ## -- Size: 5
    jar.deposit(5)

    # n < 0
    with pytest.raises(ValueError):
        jar.withdraw(-1)

    # n > size
    with pytest.raises(ValueError):
        jar.withdraw(6)

