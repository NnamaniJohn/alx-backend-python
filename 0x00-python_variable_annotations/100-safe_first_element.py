#!/usr/bin/env python3
"""
safe first element
"""
import typing


def safe_first_element(lst: typing.Sequence[typing.Any])\
        -> typing.Union[typing.Any, None]:
    """
    safe_first_element
    :param lst:
    :return:
    """
    if lst:
        return lst[0]
    else:
        return None
