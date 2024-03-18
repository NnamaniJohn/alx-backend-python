#!/usr/bin/env python3
"""
basic async syntax
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    basic async syntax
    :param max_delay:
    :return:
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
