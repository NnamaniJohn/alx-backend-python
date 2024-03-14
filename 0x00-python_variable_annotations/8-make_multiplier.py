#!/usr/bin/env python3
"""
make multiplier
"""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """
    make multiplier
    :param multiplier:
    :return:
    """
    return lambda x: x * multiplier
