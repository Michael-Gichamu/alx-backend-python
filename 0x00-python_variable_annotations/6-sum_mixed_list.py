#!/usr/bin/env python3
"""Contains function sum_mixed_list"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes a list mxd_lst of integers and floats,
    returns their sum as a float.
    """
    return sum(mxd_lst)
