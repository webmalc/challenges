# Uses python3

import sys


def fractional_knapsack(capacity: int, weights: list, values: list) -> float:
    """
    A thief finds much more loot than his bag can fit. Help him to find
    the most valuable combination of items assuming that any fraction
    of a loot item can be put into his bag.

    The goal of this code problem is to implement an algorithm for
    the fractional knapsack problem.

    >>> fractional_knapsack(50, [20, 50, 30], [60, 100, 120])
    180.0

    >>> fractional_knapsack(10, [30], [500])
    166.66666666666669
    """
    value = 0.
    loot = [(x / weights[i], weights[i]) for i, x in enumerate(values)]
    loot.sort(key=lambda x: x[0], reverse=True)
    for thing in loot:
        thing_weight = thing[1] if capacity > thing[1] else capacity
        value += thing[0] * thing_weight
        capacity -= thing_weight
    return value


def get_args():
    """
    Get command line args
    """
    data = list(map(int, sys.stdin.read().split()))
    num, capacity = data[0:2]
    values = data[2:(2 * num + 2):2]
    weights = data[3:(2 * num + 2):2]

    return capacity, weights, values


if __name__ == "__main__":
    print("{:.10f}".format(fractional_knapsack(*get_args())))
