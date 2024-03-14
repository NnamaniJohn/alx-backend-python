#!/usr/bin/env python3
"""
to kv
"""
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """
    to kv
    :param k:
    :param v:
    :return:
    """
    ret: typing.Tuple[str, float] = (k, pow(v, 2))
    return ret
