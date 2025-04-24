"""A simple console-based Connect Four game in Python"""

from copy import deepcopy

from engine import ai_minimax, ai_random


def intsafeinput(text: str) -> int:
    """Function which is used to safely get an integer input"""
    while True:
        try:
            integer: int = int(input(text))
            return integer
        except ValueError:
            print("Integer input expected\n")


class FourInARow:
    """The game class containing the methods needed to run the game"""

    def __init__(self, matrix=None) -> None:
        """Initializing the game class"""
        if matrix is None:
            self.matrix: list[list[str]] = [[], [], [], [], [], [], []]
        else:
            self.matrix = matrix
        self.width: int = len(self.matrix)
        self.height: int = 6
        self.print_playfield()

    def print_playfield(self) -> None:
        """prints the matrix so the player can see what the playfield looks like
        with the current moves shown on the board"""
        print(" -----------------------")
        for x_coordinate in range(self.height - 1, -1, -1):  # x_coordinate: list[str]
            print("|", end="  ")
            for entry in self.matrix:  # entry: str
                try:
                    print(entry[x_coordinate], end="  ")
                except IndexError:
                    print("-", end="  ")
            print("|")
        print("| --------------------- |")
        print("|  1  2  3  4  5  6  7  |")
        print(" -----------------------")

    def gameplay(self) -> None:
        """gameplay loop of our connect-four game"""
        maxmoves: int = self.width * self.height
        column: int | None = None
        for counter in range(maxmoves):  # counter: int
            if counter % 2:
                symbol: str = "X"
                column = self.bot_move()
            else:
                symbol = "O"
                column = self.player_move()

            self.matrix[column].append(symbol)
            self.print_playfield()
            if self.win_test([column, len(self.matrix[column]) - 1], symbol):
                print(f"The player with the symbol '{symbol}' won the game!")
                return

    def win_test(self, coordinates, symbol) -> bool:
        """check if the game has been won by adding up matching symbols in a row"""
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
            if win_con + previous >= 3:
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
                if len(self.matrix[coordinates[0]]) > coordinates[1] >= 0:
                    if self.matrix[coordinates[0]][coordinates[1]] == symbol:
                        result += 1
                    else:
                        return result
                else:
                    return result
            else:
                return result

    def player_move(self) -> int:
        """Asking the player, which move he wants to take"""
        symbol: str = "O"
        print(f"Where do you want to put an {symbol}?")

        while True:
            column: int = intsafeinput(f"Choose column from 1 to {self.width}: ") - 1
            try:
                if len(self.matrix[column]) < self.height:
                    return column
                print("Column is filled already!\n")
            except IndexError:
                print(f"There are only {self.width} columns!\n")

    def bot_move(self) -> int:
        """Getting the move made by the ai player"""
        symbol: str = "X"
        gamestate: list = deepcopy(self.matrix)
        randomai: ai_random.Random = ai_random.Random(
            gamestate, symbol, [self.height, self.width]
        )
        column: int = randomai.random_move
        gamestate = deepcopy(self.matrix)
        minimax: ai_minimax.Minimax = ai_minimax.Minimax(
            gamestate, symbol, [self.height, self.width]
        )
        column = minimax.best_move
        return column


if __name__ == "__main__":
    game: FourInARow = FourInARow()
    game.gameplay()
    print("Thanks for playing!")
