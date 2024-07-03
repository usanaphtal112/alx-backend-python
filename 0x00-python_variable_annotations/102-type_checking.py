"""
This module demonstrates zooming in on a tuple by repeating each element based on a given factor.
"""

from typing import Tuple, List

"""
This module demonstrates zooming in on a tuple by repeating each element based on a given factor.
"""


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> Tuple[int, ...]:
    """
    Zooms in on a tuple by repeating each element a certain number of times.

    Parameters:
    lst (Tuple[int, ...]): The input tuple of integers to zoom in on.
    factor (int, optional): The factor by which each element in the tuple should be repeated. Defaults to 2.

    Returns:
    Tuple[int, ...]: A tuple containing each element of the input tuple repeated `factor` times.
    """
    zoomed_in: List[int] = [item for item in lst for i in range(factor)]
    return tuple(zoomed_in)
