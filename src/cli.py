import sys

from fizzbuzz import fizzbuzz


def parse_args() -> str:
    """Assumes cli called with python cli.py [number]"""
    _, number = sys.argv
    return number


def validate(number: str) -> int:
    assert number.isdigit(), f"Invalid number supplied: {number}"

    n = int(number)
    assert n > 0, f"Number is not positive: {n}"

    return n


def cli():
    n = validate(parse_args())
    ret = fizzbuzz(n)
    print(ret)


if __name__ == "__main__":
    cli()
