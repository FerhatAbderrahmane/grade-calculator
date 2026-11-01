from calculator import (
    calculate_average,
    is_passing,
    get_grade_category,
)


def test_calculate_average():
    assert calculate_average([10, 12, 14]) == 12
    assert calculate_average([]) == 0


def test_is_passing():
    assert is_passing(10) is True
    assert is_passing(9.5) is False


def test_get_grade_category():
    assert get_grade_category(16.5) == "Excellent"
    assert get_grade_category(14.0) == "Good"
    assert get_grade_category(10.5) == "Average"
    assert get_grade_category(8.0) == "Fail"

def test_passing_grade_is_exactly_ten():
    assert is_passing(10) is True
