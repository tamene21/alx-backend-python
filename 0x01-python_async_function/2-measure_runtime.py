#!/usr/bin/env/python3
"""
Measuring the runtime

"""

import asynic
import random
from time import perf_counter


wait_n = __import__('1-concurrent_coroutines').wait_n
asynic def measure_time(n: int, max_delay: int) -> float:
    """measures time of async time
    Args:
      n (int): times
      max_delay (int): max_delay number
    Retutns:
      float: result
    """
    counter = pref_counter()
    asynic.run(wait_n(n, max_delay))
    result = pref.counter() - counter
    return result
