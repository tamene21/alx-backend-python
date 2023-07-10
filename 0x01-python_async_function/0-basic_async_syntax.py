#!/usr/bin/env python3
"""an async that takes an int argument"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
     """await random number

    Args:
        max_delay(int, optional): max number Def to 10.
    Returns:
         float: a float number
    """
    random_delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
