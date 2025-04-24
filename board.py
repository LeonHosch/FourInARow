"""Four in a Row Game Board Module"""


class Board:
    """
    Represents the game board for Four in a Row.
    """

    def __init__(self, rows: int = 6, columns: int = 7) -> None:
        """
        Initializes the board with the given dimensions.

        :param rows: Number of rows in the board (default is 6).
        :param columns: Number of columns in the board (default is 7).
        """
        self.rows: int = rows
        self.columns: int = columns
        self.grid: list[list[str]] = [
            [" " for _ in range(columns)] for _ in range(rows)
        ]
        self.current_player: int = 1  # Current player (1 or -1)

    def switch_player(self) -> None:
        """
        Switches the current player.
        """
        self.current_player *= -1  # Switch between 1 and -1

    def drop_piece(self, column: int, piece: str) -> bool:
        """
        Drops a piece into the specified column.

        :param column: The column index where the piece is dropped.
        :param piece: The piece to drop (e.g., 'X' or 'O').
        :return: True if the piece was successfully dropped, False otherwise.
        """
        if column < 0 or column >= self.columns:
            return False
        for row in reversed(range(self.rows)):
            if self.grid[row][column] == " ":
                self.grid[row][column] = piece
                return True
        return False

    def is_full(self) -> bool:
        """
        Checks if the board is full.

        :return: True if the board is full, False otherwise.
        """
        for row in self.grid:
            if " " in row:
                return False
        return True

    def check_winner(self, piece: str) -> bool:
        """
        Checks if the given piece has won the game.

        :param piece: The piece to check (e.g., 'X' or 'O').
        :return: True if the piece has won, False otherwise.
        """
        # Check horizontal
        for row in range(self.rows):
            for col in range(self.columns - 3):
                if all(self.grid[row][col + i] == piece for i in range(4)):
                    return True

        # Check vertical
        for col in range(self.columns):
            for row in range(self.rows - 3):
                if all(self.grid[row + i][col] == piece for i in range(4)):
                    return True

        # Check diagonal (bottom-left to top-right)
        for row in range(self.rows - 3):
            for col in range(self.columns - 3):
                if all(self.grid[row + i][col + i] == piece for i in range(4)):
                    return True

        # Check diagonal (top-left to bottom-right)
        for row in range(3, self.rows):
            for col in range(self.columns - 3):
                if all(self.grid[row - i][col + i] == piece for i in range(4)):
                    return True
        return False

    def reset(self) -> None:
        """
        Resets the board to its initial empty state.
        """
        range_columns: range = range(self.columns)
        range_rows: range = range(self.rows)
        self.grid = [[" " for _ in range_columns] for _ in range_rows]

    def __str__(self) -> str:
        """
        Returns a string representation of the board.
        """
        board_str: str = ""
        for row in self.grid:
            board_str += "|".join(row) + "\n"
        board_str += "-" * (2 * self.columns - 1) + "\n"
        board_str += " ".join(map(str, range(self.columns))) + "\n"
        return board_str
