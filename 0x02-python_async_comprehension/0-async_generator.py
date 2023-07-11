#!/usr/bin/env python3
"""Async generator that loops 10 times """
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Generates 10 times"""
    for _ in range(10):
        await asyncio.asleep(1)
        yield random.random() * 10
