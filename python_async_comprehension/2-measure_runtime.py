#!/usr/bin/env python3
"""Module that measures the execution time of 4 asynchronous comprehensions"""

import asyncio
import time

async_comprehension = __import__(
    '1-async_comprehension'
).async_comprehension


async def measure_runtime() -> float:
"""Measure the total runtime of four asynchronous comprehensions running in parallel"""
    start_time = time.perf_counter()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )

    end_time = time.perf_counter()

    return end_time - start_time
