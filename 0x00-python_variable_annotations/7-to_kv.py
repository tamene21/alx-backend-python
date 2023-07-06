#!/usr/bin/env python3
"""take a string and an int OR float as arguments and returns a tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return int and float as Tuple"""
    return k, v**2
