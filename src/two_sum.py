# two_sum.py
from typing import List, Generator


def two_sum(
    num_list: List[int], expected_result: int
) -> Generator[tuple[int, int], None, None]:
    """
    two_sum function to search into a list of numbwers and if the result of addition
    operation between two different list items is equals to expected_result, then
    those numbers will be yield from a generator:

    > two_sum([2,5,6,1], 7)

    > 2,5

    > 6,1

    Params:
        - num_list: List[int] | List of numbers
        - expected_result: int | A number and this will be the result of the sum
            operation between two different numbers from 'num_list' var
    Returns:
        - num_list_i: int | First value found to the sum
        - num_list_j: int | Second value found to the sum
    """
    # look up the first element in the list
    for i in range(len(num_list) - 1):
        # look up other element in the list
        for j in range(i + 1, len(num_list)):
            # if these two elemets sum to expected_result, yield the pair elements
            if num_list[i] + num_list[j] == expected_result:
                yield num_list[i], num_list[j]
