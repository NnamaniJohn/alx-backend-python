#!/usr/bin/env python3
"""
element length
"""
import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """
    element_length
    :param lst:
    :return:
    """
    return [(i, len(i)) for i in lst]
