import random
import time

from xo.engine.board import Board
from xo.mctree.simulator import monte_carlo_tree_search

if __name__ == "__main__":
    # mainWindow = MainWindow()
    # mainWindow.start()
    sim_numbers = [1, 10, 25, 50, 80, 100]
    iterations = [5000, 500, 200, 100, 100, 50]
    simulations = 1000
    for sim, it in zip(sim_numbers, iterations):
        print("\n\n*****************Simulation*****************")
        total_losses = 0
        current_time = time.time()
        for i in range(simulations):
            board = Board()
            while board.check_game_over() is None:
                # Fac o mutare
                all_moves = board.get_none_indexes()
                random_move = random.choice(all_moves)
                board.make_move(random_move[0], random_move[1])
                if board.check_game_over():
                    if board.check_game_over() == 'X':
                        total_losses += 1
                else:
                    board = monte_carlo_tree_search(board, it, sim)
            if (i + 1) % 100 == 0:
                print("Simulation {}: Elapsed time: {:.2f} seconds".format(i + 1, (time.time() - current_time)))
        print(f"Configuration (sim_number = {sim}, iterations = {it}): Loss percent: {total_losses/simulations*100}%")
