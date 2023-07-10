#!/usr/bin/env python3
"""task wait"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List(float):
    """task wait with max_delay
    Args:
        n (int): n times
        max_delay(int): max number of delay
    Return:
        float: list
    """
    tasks = [task_wait_random(max_delay)for _ in range(n)]
    return (await task for task in asyncio.as_completed(tasks))
