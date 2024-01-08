import pygame
import time
from xo.engine.board import Board
from xo.mctree.simulator import monte_carlo_tree_search

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700
SQUARE_DIM = 200

LEFT_CLICK = 1
RIGHT_CLICK = 3

X_PLAYER_ID = 1000
O_PLAYER_ID = 1001

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)


def is_occupied(board: Board, current_x: int, current_y: int) -> bool:
    """
    check if a position on the board is occupied
    :param board: moves of the player until now
    :param current_x: current x coordinate
    :param current_y: current y coordinate
    :return: True or false value
    """
    return board.get_matrix()[current_x][current_y] is not None


class MainWindow:
    """
    The window of the game execution
    """

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("TicTacToe - MCTS")
        # Sprite load
        self._screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self._X_SPRITE = pygame.transform.scale(pygame.image.load("images/xx.png").convert_alpha(),
                                                (SQUARE_DIM, SQUARE_DIM))
        self._O_SPRITE = pygame.transform.scale(pygame.image.load("images/oo.png").convert_alpha(),
                                                (SQUARE_DIM, SQUARE_DIM))
        self._BORDER = pygame.image.load("images/border.png").convert()
        self._RESET = pygame.image.load("images/reset.png").convert_alpha()
        # Scoreboard
        self._my_font = pygame.font.SysFont("Comic Sans MS", 30)
        self._player_score = 0
        self._ai_score = 0
        # Game Engine
        self._board = Board()
        self._iterations = 100
        self._sim_number = 80
        self._run = True
        self._active = True

    def _reset_game(self) -> None:
        """
        Resets game to initial state
        :return:
        """
        self._board.reset_board()
        self._run = True
        self._active = True

    def _draw_item(self, x_pos, y_pos, player_type) -> None:
        """
        Draw an item on the board
        :param x_pos: x coordinate of the item on the screen
        :param y_pos: y coordinate of the item on the screen
        :param player_type: type of player on the board
        :return:
        """
        sprite = self._X_SPRITE if player_type == "X" else self._O_SPRITE
        self._screen.blit(sprite, (x_pos * SQUARE_DIM, y_pos * SQUARE_DIM))

    def start(self) -> None:
        """
        Starts and runs the game
        :return:
        """
        clock = pygame.time.Clock()
        while self._run:
            # Draw screen
            self._screen.fill(COLOR_WHITE)
            table = self._board.get_matrix()
            for i in range(3):
                for j in range(3):
                    if table[i][j] is not None:
                        self._draw_item(i, j, table[i][j])
            self._screen.blit(self._BORDER, (0, 600))
            self._screen.blit(self._RESET, (450, 640))
            self._screen.blit(self._my_font.render(f"Player {self._player_score} - {self._ai_score} AI",
                                                   True, COLOR_BLACK), (50, 637))

            events_list = pygame.event.get()

            for event in events_list:
                if event.type == pygame.QUIT:
                    self._run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    # print(f"Event: clicked mouse_pos: {mouse_pos[0]}, {mouse_pos[1]}")
                    if event.button == LEFT_CLICK and 450 <= mouse_pos[0] <= 550 and 640 <= mouse_pos[1] <= 680:
                        self._reset_game()

            if self._active:
                for event in events_list:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        mouse_x = mouse_pos[0] // SQUARE_DIM * SQUARE_DIM
                        mouse_y = mouse_pos[1] // SQUARE_DIM * SQUARE_DIM

                        if mouse_pos[0] > SCREEN_WIDTH or mouse_pos[1] > SCREEN_WIDTH:
                            continue

                        if event.button == LEFT_CLICK:
                            if not is_occupied(self._board, mouse_x // SQUARE_DIM, mouse_y // SQUARE_DIM):
                                # Make player move
                                self._board.make_move(mouse_x // SQUARE_DIM, mouse_y // SQUARE_DIM)
                                self._draw_item(mouse_x // SQUARE_DIM, mouse_y // SQUARE_DIM, 'X')
                                pygame.display.update()
                                self._active = self._board.check_game_over() is None
                                # Make AI move if the game is not finished
                                if self._active:
                                    pygame.time.wait(500)
                                    # -----------------------Monte Carlo Search Tree-------------------------
                                    current_time = time.time()
                                    self._board = monte_carlo_tree_search(self._board, self._iterations,
                                                                          self._sim_number)
                                    print("Elapsed time: %.2f seconds." % (time.time() - current_time))
                                    # -----------------------------------------------------------------------
                                    self._active = self._board.check_game_over() is None
                                # If the game is over, update it
                                if not self._active:
                                    if self._board.check_game_over() == 'X':
                                        self._player_score += 1
                                    elif self._board.check_game_over() == '0':
                                        self._ai_score += 1
                                    self._screen.blit(self._my_font.render(f"Player {self._player_score} - "
                                                                           f"{self._ai_score} AI", True, COLOR_BLACK),
                                                      (50, 637))

            pygame.display.update()
            clock.tick(60)

        pygame.quit()
