"""
The graph module
"""
import os
import pickle
from typing import Dict, List

from networkx.classes import Graph


class WordsGraphs():
    """
    Storage for the word graphs
    """

    max_length: int = 6
    min_length: int = 3
    graphs: Dict[int, Graph] = {}

    def get_graph(self, word_len: int) -> Graph:
        """
        Get a graph by the word length
        """
        return self.graphs.get(word_len, Graph())

    def load_words(self, words: list) -> None:
        """
        Load the words in to graphs
        """
        self._add_nodes(words)
        self._add_edges()

    def _add_edges(self) -> None:
        """
        Add edges to graphs
        """
        for i in range(self.min_length, self.max_length + 1):
            print('Process the words with length {}'.format(i))
            graph = self.get_graph(i)
            for node in graph.nodes():
                for word in graph.nodes():
                    if self._compare_words(node, word):
                        graph.add_edge(node, word)

    @staticmethod
    def _compare_words(word1: str, word2: str) -> bool:
        """
        Check if the words are able to be edges
        """
        if len(word1) != len(word2):
            return False
        result = 0
        for k, char in enumerate(word1):
            if word2[k] != char:
                result += 1
            if result > 1:
                return False

        return result == 1

    def _add_nodes(self, words: list) -> None:
        """
        Add nodes to graphs
        """
        for word in words:
            word_len = len(word)
            graph = self.get_graph(word_len)
            graph.add_node(word)
            self.graphs[word_len] = graph


class Database():
    """
    DB for the graphs
    """
    words_path: str = './english-words/words_alpha.txt'
    db_dir: str = 'db'
    db_filename: str = db_dir + '/graph_{}'

    def load_words_from_file(self) -> List[str]:
        """
        Load the words list as a list
        """
        with open(self.words_path) as file:
            return file.read().splitlines()

    def save_graphs(self, graphs: WordsGraphs):
        """
        Save the graph to the file
        """
        os.makedirs(self.db_dir)
        for i, graph in graphs.graphs.items():
            with open(self.db_filename.format(i), 'wb') as file:
                pickle.dump(graph, file)

    def load_graphs(self):
        """
        Load the graph from the file
        """
        graphs = WordsGraphs()
        for filename in os.listdir(self.db_dir):
            with open(os.path.join(self.db_dir, filename), 'rb') as file:
                graphs.graphs[int(filename.split('_')[1])] = pickle.load(file)
        return graphs

    def get_graphs(self) -> WordsGraphs:
        """
        Get a WordsGraphs instance
        """
        if not os.path.isdir(self.db_dir):
            print('Loading words from the list...')
            words = self.load_words_from_file()
            graphs = WordsGraphs()
            graphs.load_words(words)

            self.save_graphs(graphs)
            return graphs

        return self.load_graphs()


if __name__ == "__main__":
    DATABASE = Database()
    DATABASE.get_graphs()
