#!/usr/bin/env python3
"""Contains function element_length"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotation of this function to return values with appropriate types."""
    return [(i, len(i)) for i in lst]
