import copy
import random

from xo.engine.board import Board
from xo.mctree.node import Node

X_PLAYER_ID = 1000
O_PLAYER_ID = 1001


def check_different_boards(state1: Board, state2: Board) -> bool:
    """
    Checks if two boards are distinct
    :param state1: first state
    :param state2: second state
    :return: true or false
    """
    board1 = state1.get_matrix()
    board2 = state2.get_matrix()
    return sum(1 for i in range(3) for j in range(3) if board1[i][j] != board2[i][j]) > 0


def check_distinct_child(state: Board, children: list[Node]) -> bool:
    """
    Checks if a new configuration is different with his brothers
    :param state: new state of the board
    :param children: a list with children
    :return: true or false
    """
    return all(check_different_boards(state, child.state) for child in children)


def game_simulation(state: Board, results: dict) -> None:
    """
    Simulate a singular game execution
    :param state: current state of the game
    :param results: dictionary with results
    :return:
    """
    clone_state = copy.deepcopy(state)
    while not clone_state.check_game_over():
        empty_cells = clone_state.get_none_indexes()
        next_move = random.choice(empty_cells)
        clone_state.make_move(next_move[0], next_move[1])
    # Update result
    if clone_state.check_game_over() != 'D':
        results[clone_state.check_game_over()] += 1
    else:
        results['X'] += 1
        results['0'] += 1


def random_simulations(state: Board, sim_number: int) -> any:
    """
    Simulate a number of game executions
    :param sim_number: number of random simulations
    :param state: current state of the game
    :return: gameover status
    """
    results = {'X': 0, '0': 0, 'O': 0}

    for _ in range(sim_number):
        # threads = list()
        # lock = Lock()
        game_simulation(state, results)
    return results


def monte_carlo_tree_search(initial_state: Board, iterations: int, sim_number: int) -> Board:
    """
    Runs a Monte Carlo Tree Search algorithm with configuration
    :param sim_number: number of random simulations
    :param initial_state: current state of the board
    :param iterations: the number of iterations
    :return: the new board with the best move to play for AI
    """
    root = Node(initial_state)
    for _ in range(iterations):
        node = root
        state = initial_state

        # Selection
        while not state.check_game_over() and node.is_fully_expanded() and len(node.children) > 0:
            node = node.get_best_child()
            state = copy.deepcopy(node.state)

        # Expansion
        if not node.is_fully_expanded() and not node.state.check_game_over():
            empty_cells = state.get_none_indexes()
            # Keep generate new vales until I find a new son
            while True:
                random_empty_cell = random.choice(empty_cells)
                new_state = copy.deepcopy(state)
                new_state.make_move(random_empty_cell[0], random_empty_cell[1])

                if check_distinct_child(new_state, node.children):
                    new_node = Node(new_state, parent=node)
                    node.children.append(new_node)
                    node = new_node
                    break

        # Simulation
        state = node.state
        results = random_simulations(state, sim_number)

        # Backpropagation
        while node is not None:
            node.visits += 1
            current_player = '0' if node.state.get_turn() == X_PLAYER_ID else 'X'
            node.wins += results[current_player]
            node = node.parent

    return root.get_best_child().state
