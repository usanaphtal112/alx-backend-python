"""
Define a TypeVar for the return type, which can be any type or None
"""

from typing import Sequence, Any, Union

"""
Define a TypeVar for the return type, which can be any type or None
"""


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a sequence if it exists, otherwise returns None.

    Parameters:
    lst (Sequence[Any]): A sequence of elements of any type.

    Returns:
    Union[Any, None]: The first element of the sequence or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
