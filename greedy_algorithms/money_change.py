# Uses python3


def money_change(amount: int) -> int:
    """
    The goal in this problem is to find the minimum number of coins needed
    to change the input value (an integer) into coins
    with denominations 1, 5, and 10.

    (2 = 1 + 1)
    >>> money_change(2)
    2

    (28 = 10 + 10 + 5 + 1 + 1 + 1)
    >>> money_change(28)
    6
    """
    result = 0
    denomintations = [10, 5, 1]
    for i in denomintations:
        if amount >= i:
            result += amount // i
            amount = amount % i

    return result


if __name__ == '__main__':
    print(money_change(int(input())))
