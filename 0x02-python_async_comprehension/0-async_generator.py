#!/usr/bin/env python3
"""
async generator
"""
import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """
    async generator
    :return:
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
