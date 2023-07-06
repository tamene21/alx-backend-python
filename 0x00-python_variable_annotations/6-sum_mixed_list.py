#!/usr/bin/env python3
"""Contains mixed-list list of integers and float & return a sum as a float"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return a sum of int and float values as float"""
    return sum(mxd_lst)
