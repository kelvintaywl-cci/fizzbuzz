from typing import Union


def fizzbuzz(n: int) -> Union[str, int]:
    shoutout = ""
    if n % 3 == 0:
        shoutout += "FIZZ"
    if n % 5 == 0:
        shoutout += "BUZZ"

    return shoutout or n
