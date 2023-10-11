#!/usr/bin/env python3
""" Measure times """
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
        measure time and execute in paralallel

        Args:
            void

        Return:
            float random numbers
    """
    start_time = time.time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.time()

    return (end_time - start_time)