# app.py
import sys

from two_sum import two_sum
from utils import load_cli_args


def main() -> None:
    try:
        num_list, expected_result = load_cli_args(sys.argv)
    except:
        print("Input arguments are incorrect. Please read README.md")
        sys.exit(1)
    for a, b in two_sum(num_list, expected_result):
        print(f"{a}, {b}")


if __name__ == "__main__":
    main()
