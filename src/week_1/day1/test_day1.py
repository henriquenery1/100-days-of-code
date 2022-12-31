from day1 import calc_age_days

def test_calc_age_days():
    result = calc_age_days(0)
    assert result == 0, f"Expected 0, but got {result}"

def test_calc_age_days():
    result = calc_age_days(1)
    assert result == 365, f"Expected 365, but got {result}"