import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """Measures total execution time for wait_n.

    Args:
        n (int): arg for wait_n
        max_delay (int): arg for wait_n

    Returns:
        float: time elapsed.
    """
    start_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time: float = time.time()
    total_time: float = end_time - start_time
    return total_time / n
