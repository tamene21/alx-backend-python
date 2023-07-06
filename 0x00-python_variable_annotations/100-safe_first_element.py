#!/usr/bin/env python3
"""duk-typed annotation"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """retrives the first list of an element"""
    if lst:
        return lst[0]
    else:
        return None
