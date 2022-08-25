# utils.py
from typing import List


def load_cli_args(io_args: List[str]) -> tuple[List[int], int]:
    """
    load_cli_args function loads args from command line and map it to a list and to an integer.

    Params:
        - io_args: List[str] | I/O args loaded when the app is called from the terminal

    Returns:
        - num_list: List[int] | List of numbers
        - expected_result: int | A number
    """

    num_list, expected_result = io_args[1:3]
    num_list = num_list.split(",")
    num_list = list(map(lambda x: int(x), num_list))

    expected_result = int(expected_result)
    return num_list, expected_result
