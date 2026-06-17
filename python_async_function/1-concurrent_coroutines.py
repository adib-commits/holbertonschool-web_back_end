#!/usr/bin/env python3
"""Module running multiple coroutines simultaneously"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Executes wait_random n times and returns the sorted delays"""
    delays = []

    for coroutine in asyncio.as_completed(
        [wait_random(max_delay) for _ in range(n)]
    ):
        delays.append(await coroutine)

    return delays
