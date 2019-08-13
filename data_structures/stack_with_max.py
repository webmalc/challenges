#python3
import sys


class StackWithMax():
    """
    The stack class with the max method

    Stack is an abstract data type supporting the operations Push() and Pop().
    It is not difficult to implement it in a way that both these operations
    work in constant time. In this problem, you goal will be to implement
    a stack that also supports finding the maximum value and to ensure that all
    operations still work in constant time.
    """

    def __init__(self):
        self.__stack = []
        self.__max_values = []

    def push(self, element):
        """
        Add an element to the stack
        """
        self.__stack.append(element)

        if len(self.__stack) == 1:
            self.__max_values.append(element)
            return

        if element > self.__max_values[-1]:
            self.__max_values.append(element)
        else:
            self.__max_values.append(self.__max_values[-1])

    def pop(self):
        """
        Remove an element from the stack
        """
        assert self.__stack
        self.__stack.pop()
        self.__max_values.pop()

    def max(self):
        """
        Add the max element of the stack
        """
        assert self.__stack
        return self.__max_values[-1]


def _test_stack(values, pops=0):
    """
    Test the stack class

    >>> _test_stack([1, 3, 5, 6, 2, 3, 4])
    6

    >>> _test_stack([1, 3, 5, 6, 2, 3, 12])
    12

    >>> _test_stack([1, 3, 5, 6, 2, 3, 12], pops=1)
    6

    >>> _test_stack([1, 3, 5, 6, 2, 7, 12], pops=2)
    6

    >>> _test_stack([1])
    1
    """
    stack = StackWithMax()
    for val in values:
        stack.push(val)
    for _ in range(pops):
        stack.pop()

    return stack.max()


def process():
    """
    The main script
    """
    stack = StackWithMax()
    for _ in range(int(sys.stdin.readline())):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.push(int(query[1]))
        elif query[0] == "pop":
            stack.pop()
        elif query[0] == "max":
            print(stack.max())
        else:
            assert 0


if __name__ == '__main__':
    process()
