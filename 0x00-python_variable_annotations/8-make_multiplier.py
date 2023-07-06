#!/usr/bin/env python3
"""A function a multiply of a float and return a float function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """multiplies a float with multiplier"""
    def mult_func(number: float) -> float:
        return multiplier * number
    return mult_func
