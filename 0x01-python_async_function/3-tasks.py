#!/usr/bin/env python3
"""Taks an int and returns task list"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Task will be returned
    Args:
        max_delay(int): max delay number
    Return:
        asyncio.Task: return a task
    """
    return asynico.create_task(wait_random(max_delay))
