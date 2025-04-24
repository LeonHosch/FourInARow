"""A simple console-based Connect Four game in Python"""

from random import randint
from time import sleep

from classes import safe_inputs as Safe
from classes.show_board import ShowBoard
from engine import ai_random


def custom_game() -> list[int]:
    """Create a game with custom parameters"""
    while True:
        width: int = Safe.int_safe_input(
            "How many columns do you want to have: ", 4, 20
        )
        height: int = Safe.int_safe_input(
            "How high do you want the rows to be: ", 4, 20
        )
        win_condition: int = Safe.int_safe_input(
            "How many in a row should be needed to win: ", 3, max(width, height)
        )
        return [width, height, win_condition]


class FourInARow:
    """The game class containing the methods needed to run the game"""

    def __init__(self, width: int = 7, height: int = 6, win_condition: int = 4) -> None:
        """Initializing the game class"""
        self.width: int = width
        self.height: int = height
        self.win_condition: int = win_condition - 1
        self.matrix: list[list[str]] = [
            ["-" for _ in range(height)] for _ in range(width)
        ]
        self.board: ShowBoard = ShowBoard(self.matrix, width, height)
        self.is_finished: bool = False
        self.out_of_moves = False

    def load_board(self, newmatrix: list[list[str]]) -> None:
        """can load a custom matrix into the game"""
        if len(newmatrix) >= 1:
            self.matrix = newmatrix
            self.board.change_values(len(self.matrix), len(self.matrix[0]), self.matrix)

    def gameplay(self) -> None:
        """gameplay loop of our connect-four game"""
        counter = randint(1, 2)
        while not self.is_finished:  # counter: int
            if counter == 1:
                sleep(2)
                self.bot_move()
                counter = 2
            else:
                self.player_move()
                counter = 1
            self.check_finished()
        if self.out_of_moves:
            print("The game ended in a draw!")

    def player_move(self) -> None:
        """Asking the player, which move he wants to take"""
        symbol: str = "O"
        print(f"Where do you want to put an {symbol}?")
        while True:
            column: int = (
                Safe.int_safe_input(
                    f"Choose column from 1 to {self.width}: ", 1, self.width
                )
                - 1
            )
            if "-" in self.matrix[column]:
                self.place_symbol(column, symbol)
                return

    def bot_move(self) -> None:
        """Getting the move made by the ai player"""
        symbol: str = "X"
        gamestate: list = self.matrix
        randomai: ai_random.Random = ai_random.Random(
            gamestate, symbol, [self.height, self.width]
        )
        column: int = randomai.random_move
        self.place_symbol(column, symbol)

    def place_symbol(self, column, symbol: str) -> None:
        """Remove the first '-' in the list and replace it with the symbol"""
        replace_position: int = self.matrix[column].index("-")
        self.matrix[column][replace_position] = symbol
        self.board.print_playfield(self.matrix)
        if self.win_test([column, replace_position]):
            print(f"The player with the symbol '{symbol}' won the game!")
            self.is_finished = True

    def check_finished(self) -> None:
        """Checks if all the possible moves have been played already"""
        for column in self.matrix:
            if "-" in column:
                return
        self.is_finished = True
        self.out_of_moves = True

    def win_test(self, coordinates) -> bool:
        """check if the game has been won by adding up matching symbols in a row"""
        symbol: str = self.matrix[coordinates[0]][coordinates[1]]
        directions: list = [
            (-1, 0),
            (1, 0),
            (-1, -1),
            (1, 1),
            (1, -1),
            (-1, 1),
            (0, -1),
        ]
        counter: int = 0
        previous: int = 0
        for direction in directions:  # direction: tuple[int]
            win_con: int = self.direction_check(
                direction, symbol, [coordinates[0], coordinates[1]]
            )
            if win_con + previous >= self.win_condition:
                return True
            if counter % 2:
                previous = 0
            else:
                previous = win_con
            counter += 1
        return False

    def direction_check(self, direction, symbol, coordinates) -> int:
        """check the given direction for matching symbols"""
        result: int = 0
        while True:
            coordinates[0] += direction[0]
            coordinates[1] += direction[1]
            if self.width > coordinates[0] >= 0:
                if self.height > coordinates[1] >= 0:
                    if self.matrix[coordinates[0]][coordinates[1]] == symbol:
                        result += 1
                    else:
                        return result
                else:
                    return result
            else:
                return result


if __name__ == "__main__":
    gamemode: int = Safe.int_safe_input(
        "Which gamemode do you want to play?\n1) Standard\n2) Custom\nInput: ", 1, 2
    )
    if gamemode == 1:
        game: FourInARow = FourInARow()
    else:
        settings = custom_game()
        game: FourInARow = FourInARow(settings[0], settings[1], settings[2])

    game.gameplay()
    print("Thanks for playing!")
