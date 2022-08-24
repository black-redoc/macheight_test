from .two_sum import two_sum


def test_two_sum():
    num_list = [5, 2, 6, 1, 4, 3]
    expected_result = 7
    generator = two_sum(num_list, expected_result)
    a, b = next(generator)
    x, y = next(generator)

    assert a + b == expected_result
    assert x + y == expected_result
    assert not x == a and not y == b
