from scr.main import conversion_date

def test_get_is_digit():
    assert conversion_date("2019-01-05T00:52:30.108534") == "5.1.2019"
    assert conversion_date("2018-01-13T13:00:58.458625") == "13.1.2018"