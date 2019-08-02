# python3
import sys
from typing import List


def compute_min_refills(distance: int, tank: int, stops: List[int]):
    """
    You are going to travel to another city that is located d miles away from
    your home city. Your can can travel at most m miles on a full tank and you
    start with a full tank. Along your way, there are gas stations at distances
    stop 1 , stop 2 , . . . , stop n from your home city.
    What is the minimum number of refills needed?

    >>> compute_min_refills(950, 400, [200, 375, 550, 750])
    2

    >>> compute_min_refills(10, 3, [1, 2, 5, 9])
    -1
    """
    current = 0
    steps = 0
    stops.append(distance)
    for i, point in enumerate(stops):
        next_point = None if len(stops) <= i + 1 else stops[i + 1]
        current_statement = point - current <= tank
        next_statement = not next_point or next_point - current > tank
        if current_statement and next_statement:
            steps += 1
            current = point

    return steps - 1 if current == distance else -1


def get_args():
    """
    Get command line args
    """

    distance, tank, _, *stops = map(int, sys.stdin.read().split())
    return distance, tank, stops


if __name__ == '__main__':
    print(compute_min_refills(*get_args()))
