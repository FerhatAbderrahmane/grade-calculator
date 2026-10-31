from calculator import calculate_average, is_passing


def test_calculate_average():
    assert calculate_average([10, 12, 14]) == 12
    assert calculate_average([]) == 0


def test_is_passing():
    assert is_passing(10) is True
    assert is_passing(9.5) is False