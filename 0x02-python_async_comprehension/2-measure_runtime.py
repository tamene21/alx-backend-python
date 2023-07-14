#!/usr/bin/en python3
"""runing many comprhensions"""
import asyncio
import time
from importlib import import_module as using


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    print("One", end=" ")
    await asyncio.sleep(1)


async def main():
    await asyncio.gather(measure_runtime())


if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"\n{execution_time:0.2f}.")
