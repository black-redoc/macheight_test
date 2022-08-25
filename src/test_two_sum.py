from .two_sum import two_sum


def test_two_sum_if_a_and_b_sum_to_expected():
    num_list = [5, 2, 6, 1, 4, 3]
    expected_result = 7
    generator = two_sum(num_list, expected_result)
    a, b = next(generator)

    assert a + b == expected_result


def test_two_sum_if_x_and_y_sum_to_expected():
    num_list = [5, 2, 6, 1, 4, 3]
    expected_result = 7
    generator = two_sum(num_list, expected_result)
    _, _ = next(generator)
    x, y = next(generator)

    assert x + y == expected_result


def test_two_sum_if_returned_values_are_diferents():
    num_list = [5, 2, 6, 1, 4, 3]
    expected_result = 7
    generator = two_sum(num_list, expected_result)
    a, b = next(generator)
    x, y = next(generator)

    assert not x == a and not y == b
