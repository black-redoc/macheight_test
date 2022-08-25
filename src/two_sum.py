# two_sum.py
from typing import List, Generator


def two_sum(
    num_list: List[int], expected_result: int
) -> Generator[tuple[int, int], None, None]:
    """
    two_sum function search two numbers and their sum must be expected result.

    Params:
        - num_list: List[int] | List of numbers
        - expected_result: int | A number and this will be the result of the sum
            operation between two different numbers from 'num_list' var

    Returns:
        - num_list_i: int | First value found to the sum
        - complement: int | Second value found to the sum
    """
    complements = []
    for i in range(len(num_list) - 1):
        complement = expected_result - num_list[i]
        if complement in complements:
            yield num_list[i], complement
        else:
            complements.append(num_list[i])
