from scr.utils import get_hidden_score,get_hidden_card,get_is_digit,check_on_score

def test_get_is_digit():
    assert get_is_digit("123Test") == "123"
    assert get_is_digit("G17get4") == "174"

def test_get_hidden_card():
    assert get_hidden_card("2842877533549012") == "2842 87** **** 9012"
    assert get_hidden_card("6086997013848217") == "6086 99** **** 8217"

def test_get_hidden_score():
    assert get_hidden_score("2842877533542869") == "**2869"
    assert get_hidden_score("6086997013848217") == "**8217"

def test_check_on_score():
    assert check_on_score("Счет 2842877533542869") == "Счет **2869"
    assert check_on_score("Visa Classic 2842877533542869") == "Visa Classic 2842 87** **** 2869"
