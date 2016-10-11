#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""task_04 docstring"""


def process_data(data):
    """Fuction to calculate the sum and average of your data.

    Args:
        data (list or tuple): a list or tuple of numbers.

    Returns:
        tuple: total sum of the data, average of the data in float point
        precision.

    Examples:
        >>>process_data(1, 2, 3)
        (6, 2.0)
    """

    count = 0
    total = 0
    for list_item in data:
        count += 1
        total = total + list_item

    avg = total/count
    return (total, total / float(len(avg)))
