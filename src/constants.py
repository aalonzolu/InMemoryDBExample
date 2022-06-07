from typing import Union

VALID_TYPES = [str, int, float]
VALID_TYPES_UNION = Union[str, int, float]


class NoTransaction(Exception):
    pass


class InvalidInput(Exception):
    pass


class InvalidCommand(Exception):
    pass
