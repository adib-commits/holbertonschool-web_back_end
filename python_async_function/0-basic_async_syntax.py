#!/usr/bin/env python3
"""Module containing a coroutine that waits for a random delay"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay and then return that delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
