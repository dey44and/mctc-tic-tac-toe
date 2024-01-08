X_PLAYER_ID = 1000
O_PLAYER_ID = 1001


class Board(object):
    """
    Represents current state of the game
    """
    def __init__(self):
        self._board_state = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
        self._turn = X_PLAYER_ID

    def reset_board(self) -> None:
        """
        Reset board of the game
        :return:
        """
        self._board_state = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
        self._turn = X_PLAYER_ID

    def get_matrix(self) -> list:
        """
        Get current state of the game as a matrix
        :return: the matrix requested
        """
        return self._board_state

    def get_turn(self) -> int:
        """
        Get current turn of the game
        :return: the player who is next to move
        """
        return self._turn

    def make_move(self, x: int, y: int) -> None:
        """
        Update state of the game
        :param x: x coordinate of the player
        :param y: y coordinate of the player
        :return:
        """
        self._board_state[x][y] = 'X' if self._turn == X_PLAYER_ID else '0'
        self._turn = O_PLAYER_ID if self._board_state[x][y] == 'X' else X_PLAYER_ID

    def get_none_indexes(self) -> list:
        """
        Get a list of pairs of indexes where the matrix _board_state has None values
        :return: List of index pairs
        """
        none_indexes = [(i, j) for i in range(3) for j in range(3) if self._board_state[i][j] is None]
        return none_indexes

    def check_game_over(self) -> any:
        """
        check if the game is over
        :return: the status of the game
        """
        if self._board_state[0][0] == self._board_state[1][1] == self._board_state[2][2] is not None:
            # print(f"End: {self._board_state[0][0]}  WON!")
            return self._board_state[0][0]

        if self._board_state[0][2] == self._board_state[1][1] == self._board_state[2][0] is not None:
            # print(f"End: {self._board_state[0][2]}  WON!")
            return self._board_state[0][2]

        for i in range(0, 3):
            if self._board_state[i][0] == self._board_state[i][1] == self._board_state[i][2] is not None:
                # print(f"End: {self._board_state[i][0]}  WON!")
                return self._board_state[i][0]

            if self._board_state[0][i] == self._board_state[1][i] == self._board_state[2][i] is not None:
                # print(f"End: {self._board_state[0][i]}  WON!")
                return self._board_state[0][i]

        count = sum(1 for i in range(3) for j in range(3) if self._board_state[i][j] is not None)
        return 'D' if count == 9 else None
