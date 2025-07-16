"""A class for the negamax ai player algorithm"""

from random import randint


IS_WON: int = 1_000_000


class Negamax:
    """The class containing the methods for the negamax ai player"""

    def __init__(
        self,
        gameboard: list[list[str]],
        symbol: str,
        further: int = 5,
        bot: bool = True,
    ) -> None:
        self.gameboard: list[list[str]] = gameboard
        self.points: int = 0
        self.symbol: str = symbol
        self.opposite_symbol: str = "-"
        self.set_opposite()
        self.further: int = further
        self.bot: bool = bot
        self.best_move: int = self.evaluate_moves()

    def set_opposite(self) -> None:
        """Setting the opposite of self.bot and symbol"""
        if self.symbol == "X":
            self.opposite_symbol = "O"
        else:
            self.opposite_symbol = "X"

    def check_horizontal(self) -> int:
        """Checking the board horizontally and adding points accordingly"""
        temp_points: int = 0
        for level in range(6):
            previous: str | None = None
            max_in_row: int = 0
            in_row: int = 0
            for column in self.gameboard:
                if column[level] == previous == self.symbol:
                    in_row += 1
                    if max_in_row < in_row:
                        max_in_row = in_row
                else:
                    in_row = 0
                previous = column[level]
            if max_in_row >= 3:
                temp_points += 10000000
            else:
                temp_points += max_in_row * max_in_row
        return temp_points

    def check_vertical(self) -> int:
        """Checks the gameboard vertically and adding points accordingly"""
        temp_points: int = 0
        for column in self.gameboard:
            previous: str | None = None
            in_row: int = 0
            for value in column:
                if value == "-":
                    break
                if previous == value == self.symbol:
                    in_row += 1
                else:
                    in_row = 0
                previous = value
            if in_row >= 3:
                temp_points += 10000000
            else:
                temp_points += in_row * in_row
        return temp_points

    def evaluate_moves(self) -> int:
        """Checks future scenarios and returns the number
        for the most valuable play"""
        best_move: int = randint(0, 6)
        best_points: int = -10000000
        for number in range(7):
            if "-" in self.gameboard[number]:
                index = self.gameboard[number].index("-")
                self.gameboard[number][index] = self.symbol
                temp_points: int = 0
                temp_points += self.check_horizontal()
                temp_points += self.check_vertical()
                if temp_points <= IS_WON:
                    if self.further:
                        current_cycle = Negamax(
                            self.gameboard,
                            self.opposite_symbol,
                            self.further - 1,
                            not self.bot,
                        )
                        temp_points += current_cycle.points
                    if temp_points > best_points:
                        best_points = temp_points
                        best_move = number
                else:
                    best_points = temp_points
                    best_move = number
                    self.gameboard[number][index] = "-"
                    break
                self.gameboard[number][index] = "-"
        if not self.bot:
            best_points = -best_points
        self.points += best_points
        return best_move
