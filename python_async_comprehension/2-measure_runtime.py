#!/usr/bin/env python3
"""Module that measures the execution time of 4 asynchronous comprehensions"""

import asyncio
import time

async_comprehension = __import__(
    '1-async_comprehension'
).async_comprehension


async def measure_runtime() -> float:
    """Measures the execution time of 4 async_comprehensions in parallel"""
    start_time = time.perf_counter()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )

    end_time = time.perf_counter()

    return end_time - start_time
