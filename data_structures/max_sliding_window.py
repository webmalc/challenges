# python3
from collections import deque


def max_sliding_window(sequence, window_size):
    """
    Given a sequence a 1 , . . . , a n of integers and an integer m ≤ n,
    find the maximum among {a i , . . . , a i+m−1 } for every
    1 ≤ i ≤ n − m + 1. A naive O(nm) algorithm for solving this problem scans
    each window separately. Your goal is to design an O(n) algorithm.

    >>> max_sliding_window([2, 7, 3, 1, 5, 2, 6, 2], 4)
    [7, 7, 5, 6, 6]
    """
    queue = deque()
    length = len(sequence)
    result = []

    for i in range(window_size):
        while queue and sequence[i] >= sequence[queue[-1]]:
            queue.pop()
        queue.append(i)

    for i in range(window_size, length):
        result.append(sequence[queue[0]])
        while queue and queue[0] <= i - window_size:
            queue.popleft()
        while queue and sequence[i] >= sequence[queue[-1]]:
            queue.pop()

        queue.append(i)

    result.append(sequence[queue[0]])

    return result


def get_args():
    """
    Get command line args
    """
    num = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == num
    window_size = int(input())

    return input_sequence, window_size


if __name__ == '__main__':
    print(*max_sliding_window(*get_args()))
