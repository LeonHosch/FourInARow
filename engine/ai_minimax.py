"""The class for the minimax computer player"""

from copy import deepcopy
from random import randint


class Minimax:
    """The computer minimax player"""

    def __init__(
        self,
        gamestate: list[list[str]],
        symbol: str,
        boardsize: list[int],
        repeat: bool = True,
    ) -> None:
        """Initializing the class for the needed parameters"""
        self.gamestate: list[list[str]] = gamestate
        self.points: int = 0
        self.symbol: str = symbol
        self.height: int = boardsize[0]
        self.width: int = boardsize[1]
        self.repeat: bool = repeat
        self.best_move: int | None = None
        self.minimax_logic()

    def minimax_logic(self) -> None:
        """Either execute simulate_move or evaluate_board based on self.repeat"""
        if self.repeat:
            self.simulate_move()
        else:
            self.evaluate_board()

    def evaluate_board(self) -> None:
        """Check the board, evaluate and assign points accordingly"""
        self.points += self.check_vertical()
        self.points += self.check_horizontal()

    def check_vertical(self) -> int:
        """Check the board and give points checking the y axis"""
        for column in self.gamestate:  # list[str]
            remaining_plays: int = 6 - len(column)
            previous: str | None = None
            match_in_row: int = 0
            vertical_points: int = 0
            for matrix_value in column:  # matrix_value: str
                match_in_row = self.check_match(previous, matrix_value, match_in_row)
                previous = matrix_value
            if remaining_plays + match_in_row < 3:
                vertical_points -= 8
            else:
                vertical_points += int(match_in_row * match_in_row)
        return vertical_points

    def check_horizontal(self) -> int:
        """Check the board and give points checking the x axis"""
        for row in range(self.height):
            previous: str | None = None
            previous_in_row: int = 0
            match_in_row: int = 0
            possible_in_row: int = 0
            horizontal_points: int = 0
            for column in self.gamestate:  # column: list[str]
                try:
                    matrix_value: str | None = column[row]
                except IndexError:
                    matrix_value = None
                match_in_row = self.check_match(previous, matrix_value, match_in_row)
                if previous_in_row == match_in_row > 0:
                    possible_in_row += 1
                possible_in_row = max(possible_in_row, match_in_row)
                previous_in_row = match_in_row
                previous = matrix_value
            if possible_in_row < 3:
                horizontal_points -= 8
            else:
                horizontal_points += int(match_in_row * match_in_row)
        return horizontal_points

    def check_match(
        self, previous: str | None, entry: str | None, match_in_row: int
    ) -> int:
        """Checks if the given symbol is given multiple times in a row"""
        if self.symbol == previous == entry:
            return match_in_row + 1
        if entry is None:
            return match_in_row
        return 0

    def simulate_move(self) -> None:
        """Simulating future board states"""
        highest_evaluation = 0
        best_move = randint(0, 6)
        for picked_move in range(self.width):
            gameboard = deepcopy(self.gamestate)
            if len(self.gamestate[picked_move]) < self.height:
                gameboard[picked_move].append(self.symbol)
                evaluation = Minimax(
                    gameboard, self.symbol, [self.height, self.width], False
                )
                if evaluation.points > highest_evaluation:
                    highest_evaluation = evaluation.points
                    best_move = picked_move
        self.best_move = best_move
