# utils.py
from typing import List


def load_cli_args(io_args: List[str]) -> tuple[List[int], int]:
    """
    load_cli_args function to load I/O args and map them to the expected output,
    a tuple with a List of integers and an integer.
    Params:
        - io_args: List[str] | I/O args loaded when the app is called from the terminal
    Returns:
        - num_list: List[int] | List of numbers
        - expected_result: int | A number
    """
    # split the io_args list int two strings
    num_list, expected_result = io_args[1:]
    # split the num_list string into a list of chars separating each value with a ','
    num_list = num_list.split(",")
    # map each value from the mum_list to an integer
    num_list = list(map(lambda x: int(x), num_list))
    # cast the expected value to an integer
    expected_result = int(expected_result)
    return num_list, expected_result
