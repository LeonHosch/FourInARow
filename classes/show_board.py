"""Methods to help show the game to the player"""


class ShowBoard:
    """Class that can calculate and print the board correctly"""

    def __init__(self, matrix: list[list[str]], width: int, height: int) -> None:
        self.width: int = width
        self.height: int = height
        self.breaker: str = self.calculate_breaker()
        self.column_numbers: str = self.calculate_column_numbers()
        self.print_playfield(matrix)

    def print_playfield(self, matrix: list[list[str]]) -> None:
        """prints the matrix so the player can see what the playfield looks like
        with the current moves shown on the board"""
        print(self.breaker)
        print(self.calculate_board(matrix), end="")
        print(self.breaker)
        print(self.column_numbers)
        print(self.breaker)

    def calculate_breaker(self) -> str:
        """Calculates the string to show the breaker line"""
        breaker: str = " "
        for _ in range(self.width):
            breaker += "---"
        breaker += "--"
        return breaker

    def calculate_column_numbers(self) -> str:
        """Calculates the string to show the column numbers"""
        column_numbers: str = "|  "
        for column_number in range(1, self.width + 1):
            column_numbers += f"{column_number}  "
        column_numbers += "|"
        return column_numbers

    def calculate_board(self, matrix: list[list[str]]) -> str:
        """Calculates the string to print the board"""
        board: str = ""
        for row in range(self.height - 1, -1, -1):  # y_coordinate: int
            board += "|  "
            for column in matrix:  # column: list[str]
                board += f"{column[row]}  "
            board += "|\n"
        return board

    def change_values(self, width: int, height: int, matrix: list[list[str]]):
        """Change the board values"""
        self.width: int = width
        self.height: int = height
        self.breaker: str = self.calculate_breaker()
        self.column_numbers: str = self.calculate_column_numbers()
        self.print_playfield(matrix)
