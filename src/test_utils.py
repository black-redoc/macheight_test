from .utils import load_cli_args
import pytest


def test_load_cli_args_loads_successfully():
    io_args = ["app.py", "5,2,6,1,4,3", "12"]
    num_list, expected_result = load_cli_args(io_args)
    assert num_list == [5, 2, 6, 1, 4, 3]
    assert expected_result == 12
    assert type(expected_result) is int


def test_load_cli_args_loads_fail():
    io_args = ["app.py"]
    expected_failure = "<ExceptionInfo ValueError('not enough values to unpack (expected 2, got 0)') tblen=2>"
    with pytest.raises(ValueError) as value_error:
        load_cli_args(io_args)
    assert str(value_error) == expected_failure
