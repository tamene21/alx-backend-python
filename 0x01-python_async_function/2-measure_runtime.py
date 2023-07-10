#!/usr/bin/env/python3
"""
Measuring the runtime

"""

import asyncio
import random
from time import perf_counter


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures time of async time
    Args:
      n (int): times
      max_delay (int): max_delay number
    Retutns:
      float: result
    """
    counter = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    result = perf_counter() - counter
    return result
