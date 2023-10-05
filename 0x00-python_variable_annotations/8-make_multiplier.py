#!/usr/bin/env python3
"""Contains function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float multiplier as argument,
    returns a function.
    """
    def multiplier_func(x: float) -> float:
        """
        Takes x as an argument and
        multiplies it by multiplier.
        """
        return x * multiplier
    return multiplier_func
