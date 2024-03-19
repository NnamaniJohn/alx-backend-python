#!/usr/bin/env python3
"""
measure runtime
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure time
    :return:
    """
    start_time = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    stop_time = time.time()
    total_time = stop_time - start_time
    return total_time
