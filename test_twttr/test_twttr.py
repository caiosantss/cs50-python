from twttr import shorten

def test_vogal():
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("Twitter") == "Twttr"
    assert shorten("AeiOu") == ""

def test_consoantes():
    assert shorten("CS50") == "CS50"
