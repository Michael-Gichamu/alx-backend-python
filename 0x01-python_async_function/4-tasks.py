#!/usr/bin/env python3
"""Contains async function task_wait_n"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List:
    """Spawns a coroutine n times.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Specified delay.

    Returns:
        List: List of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for i in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)