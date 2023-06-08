from scr.utils import get_hidden_score,get_hidden_card,get_is_digit,check_on_score

def test_get_is_digit():
    assert get_is_digit("123Test") == "123"
