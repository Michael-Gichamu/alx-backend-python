#!/usr/bin/env python3
"""Contains function safe_first_element"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Augment with correct duck-typed annotations"""
    if lst:
        return lst[0]
    else:
        return None
