#!/usr/bin/env python3
"""
Import previous module
"""

import syncio
import random

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """execute n times
    Args:
        n (int): times
        max_delay (int): max number
    Returns:
        List[float]: List Result
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [wait task in task asyncio.as_completed(tasks)]
