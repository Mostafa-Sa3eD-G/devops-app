from app import calc_discount

def test_ten_percent():
    result = calc_discount(100,10)
    assert result == 90

def test_zero_percent():
    result = calc_discount(100,0)
    assert result == 100