from math import log

from xo.engine.board import Board


class Node(object):
    """
    Node class for the tree structure
    """
    def __init__(self, state: Board, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.wins = 0
        self.visits = 0

    def is_fully_expanded(self) -> bool:
        """
        Checks if the board is fully expanded
        :return: a boolean value
        """
        return len(self.children) == len(self.state.get_none_indexes())

    def get_best_child(self, c_param=1.41):
        """
        Returns the best child
        :param c_param: coefficient for UCB exploration
        :return: the best child node
        """
        return max(self.children, key=lambda child: (
                child.wins / child.visits + c_param * pow(log(self.visits) / child.visits, 0.5)
        ) if child.visits > 0 else 0)
