"""
The words module
"""
from networkx.algorithms import shortest_path
from networkx.exception import NetworkXException

from graph import Database


def get_path():
    """
    Get the shortest path
    """
    database = Database()
    graphs = database.get_graphs()

    print('The first word:')
    word1 = input()

    print('The second word:')
    word2 = input()

    if len(word2) != len(word1):
        raise AttributeError('The words are not equal!')

    print('Result:')
    try:
        print(shortest_path(graphs.get_graph(len(word1)), word1, word2))
    except NetworkXException:
        print('The words are not found!')


if __name__ == "__main__":
    get_path()
