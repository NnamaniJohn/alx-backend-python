#!/usr/bin/env python3
"""
tasks 3
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    task_wait_random
    :param max_delay:
    :return:
    """
    return asyncio.Task(wait_random(max_delay))
