#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program ."""

from data import FRUIT


def get_cost_per_item(shoplist):
    """This function creates a dictionary.

    Args: None

    Return:
        Dictionary that reflects cost per item.

    Example:
        >>> get_cost_per_item({'Lime': 12, 'Red Pear': 4, 'Peach': 24,
                               'Beet': 1})
        {'Lime': 7.08, 'Peach': 95.76, 'Red Pear': 9.96}
    """
    return {item: FRUIT[item] * shoplist[item] for item in shoplist.iterkeys()
            if item in FRUIT}


def get_total_cost(shoplist):
    """Total cost for shoplist.

    Args:
        my_list(dict): Dictionary .

    Return: The .

    Example:
        >>> get_total_cost({'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1})
        112.80000000000001
    """
    my_list = get_cost_per_item(shoplist)
    total = sum([value for value in my_list.values()])
    return total
