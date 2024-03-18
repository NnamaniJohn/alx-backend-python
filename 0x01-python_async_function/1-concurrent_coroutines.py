#!/usr/bin/env python3
"""
concurrent coroutines
"""
import asyncio
from asyncio import Queue
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def worker(queue: Queue, max_delay: int):
    """
    worker
    :param queue:
    :param max_delay:
    :return:
    """
    delay = await wait_random(max_delay)
    await queue.put(delay)


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    wait_n
    :param n:
    :param max_delay:
    :return:
    """
    queue = Queue()
    tasks = [worker(queue, max_delay) for _ in range(n)]
    await asyncio.gather(*tasks)

    delays = []
    while not queue.empty():
        delays.append(await queue.get())

    return delays
