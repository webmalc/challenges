# Uses python3

import sys
from typing import List


def max_dot_product(profit: List[int], clicks: List[int]) -> int:
    """
    You have n ads to place on a popular Internet page. For each ad,
    you know how much is the advertiser willing to pay for one click on
    this ad. You have set up n slots on your page and estimated the expected
    number of clicks per day for each slot. Now, your goal is to distribute
    the ads among the slots to maximize the total revenue.

    >>> max_dot_product([23], [39])
    897

    >>> max_dot_product([1, 3, -5], [-2, 4, 1])
    23
    """
    profit.sort(reverse=True)
    clicks.sort(reverse=True)

    return sum([a * b for a, b in zip(profit, clicks)])


def get_args():
    """
    Get command line args
    """

    data_string = sys.stdin.read()
    data = list(map(int, data_string.split()))

    return data[1:(data[0] + 1)], data[(data[0] + 1):]


if __name__ == '__main__':
    print(max_dot_product(*get_args()))
