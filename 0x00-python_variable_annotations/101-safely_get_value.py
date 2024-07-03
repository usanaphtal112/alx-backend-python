"""
Define a TypeVar for the return type, which can be any type or None
"""

from typing import Mapping, Any, Union, TypeVar

"""
Define a TypeVar for the return type, which can be any type or None
"""
T = TypeVar("T")

"""
Define a TypeVar for the return type, which can be any type or None
"""


def safely_get_value(dct: Mapping, key: Any, default: T = None) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary-like object.

    Parameters:
    dct (Mapping): The dictionary or mapping object to retrieve the value from.
    key (Any): The key to lookup in the dictionary.
    default (Optional[T], optional): The default value to return if the key is not found.

    Returns:
    Union[Any, T]: The value corresponding to the key if found, or the default value if not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
