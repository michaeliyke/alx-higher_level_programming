#!/usr/bin/python3


def weight_average(my_list=[]):
    """returns the weighted average of all integers tuple"""
    if not my_list:
        return 0
    sum_multiples = 0
    sum_lasts = 0
    for t in my_list:
        first, last = t
        sum_multiples += first*last
        sum_lasts += last
    return sum_multiples / sum_lasts
