#!/usr/bin/env python3
"""Module for executing multiple asyncio tasks."""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Execute multiple tasks and return their delays in ascending order."""
    delays = []

    for task in asyncio.as_completed(
        [task_wait_random(max_delay) for _ in range(n)]
    ):
        delays.append(await task)

    return delays
