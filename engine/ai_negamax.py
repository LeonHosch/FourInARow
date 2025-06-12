"""A class for the negamax ai player algorithm"""

from copy import deepcopy
from random import randint


class Negamax:
    """Klasse zum negamax haten"""

    def __init__(self, gameboard, symbol, further=True) -> None:
        self.gameboard = gameboard
        self.points = 0
        self.symbol = symbol
        self.check_horizontal()
        print(self.points)
        if further:
            self.best_move = self.evaluate_moves()

    def check_horizontal(self):
        """Regt mich das hier auf man"""
        for level in range(6):
            previous = None
            max_in_row = 0
            in_row = 0
            for column in self.gameboard:
                if column[level] == previous == self.symbol:
                    in_row += 1
                    if max_in_row < in_row:
                        max_in_row = in_row
                else:
                    in_row = 0
                previous = column[level]
            if max_in_row >= 3:
                self.points += 10000000
            else:
                self.points += max_in_row * max_in_row

    def check_vertical(self):
        """Checks the gameboard vertically"""
        for column in self.gameboard:
            previous = None
            in_row = 0
            for value in column:
                if value == "-":
                    break
                if previous == value == self.symbol:
                    in_row += 1
                else:
                    in_row = 0
                previous = value
            if in_row >= 3:
                self.points += 10000000
            else:
                self.points += in_row * in_row

    def evaluate_moves(self) -> int:
        """Checks future scenarios and returns the number
        for the most valuable play"""
        best_move: int = randint(0, 6)
        best_points: int = 0
        for number in range(7):
            if "-" in self.gameboard[number]:
                index = self.gameboard[number].index("-")
                copyboard = deepcopy(self.gameboard)
                copyboard[number][index] = self.symbol
                current_cycle = Negamax(copyboard, self.symbol, False)
                if current_cycle.points > best_points:
                    best_points = current_cycle.points
                    best_move = number
        return best_move
