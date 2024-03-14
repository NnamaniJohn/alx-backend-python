#!/usr/bin/env python3
"""
safe first element
"""
import typing
from types import NoneType


def safe_first_element(lst: typing.Sequence[typing.Any])\
        -> typing.Union[typing.Any, NoneType]:
    """
    safe_first_element
    :param lst:
    :return:
    """
    if lst:
        return lst[0]
    else:
        return None
