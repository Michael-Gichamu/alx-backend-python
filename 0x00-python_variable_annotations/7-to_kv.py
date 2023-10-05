#!/usr/bin/env python3
"""Contains function to_kv"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string k and an int OR float v as arguments
    returns a tuple
    """
    return (k, v ** 2.0)
