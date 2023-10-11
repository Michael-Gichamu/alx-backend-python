import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List:
    """Spawns a coroutine n times.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Specified delay.

    Returns:
        List: List of delays in ascending order.
    """
    tasks = [wait_random(max_delay) for i in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)