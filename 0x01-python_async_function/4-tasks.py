#!/usr/bin/env python3
"""
task 4
"""
import asyncio
from asyncio import Queue
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def worker(queue: Queue, max_delay: int):
    """
    worker
    :param queue:
    :param max_delay:
    :return:
    """
    delay = await task_wait_random(max_delay)
    await queue.put(delay)


async def task_wait_n(n: int, max_delay: int) -> List[float]:
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
