#!/usr/bin/env python3
"""
safely_get_value
"""
import typing
from types import NoneType

T = typing.TypeVar('T')


def safely_get_value(dct: typing.Mapping, key: typing.Any,
                     default: typing.Union[T, NoneType] = None)\
        -> typing.Union[typing.Any, T]:
    """
    safely_get_value
    :param dct:
    :param key:
    :param default:
    :return:
    """
    if key in dct:
        return dct[key]
    else:
        return default
