#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""task_05 docstring"""


def flip_keys(to_flip):
    """To reverse the order of a list.

    Args:
        to_flip(list): list that is backward.

    Returns:
        list: list goes backward.

    Examples:
        >>>LIST = [(1, 2, 3), 'abc']
        >>>NEW = flip_keys(list)
        [(3, 2, 1), 'cba']
    """

    counter = 0
    for item in to_flip:
        to_flip = to_flip[count][::-1]
        count += 1
    return to_flip 
