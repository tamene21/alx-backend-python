#!/usr/bin/env python3
"""type annotation to a function"""
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: def = None):
    """retrive a value from a list"""
    if key in dct:
        return dct[key]
    else:
        return default
