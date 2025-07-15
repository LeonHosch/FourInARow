"""This class contains the methods for altering the history"""

from copy import deepcopy

from modules.history import History
from modules.safe_inputs import int_safe_input
from modules.show_board import ShowBoard


class ViewHistory:
    """Methods for looking through the history of a played game"""

    def __init__(
        self,
        history: History,
        width: int = 7,
        height: int = 6,
        symbol_one: str = "X",
    ):
        self.move_list: History = history
        self.current_list: History = deepcopy(self.move_list)
        self.width: int = width
        self.height: int = height
        self.symbol_one: str = symbol_one
        if self.symbol_one == "X":
            self.symbol_two: str = "O"
        else:
            self.symbol_two = "X"
        self.board_setup: ShowBoard = ShowBoard(self.convert_to_matrix(), width, height)

    def view_loop(self) -> list[list[str]]:
        """Loop to keep the user in view mode with different functions"""
        while True:
            user = int_safe_input(
                "1) Undo move\n2) Redo move\n3) Show Board\n4)"
                " Start game from current state\n5) Quit program\nInput: ",
                1,
                5,
            )
            if user == 1:
                self.move_back()
            elif user == 2:
                self.move_forward()
            elif user == 3:
                self.board_setup.print_playfield(self.convert_to_matrix())
            elif user == 4:
                return self.convert_to_matrix()
            else:
                return [["Quit"]]

    def move_back(self) -> None:
        """Undo a move and show the board"""
        self.current_list.undo_last_ply()
        print(str(self.current_list))

    def move_forward(self) -> None:
        """Redo a move and show the board"""
        if self.move_list.moves:
            if self.current_list.moves:
                len_current = len(self.current_list.moves) - 1
                len_moves = len(self.move_list.moves) - 1
                if len_moves == len_current:
                    if len(self.move_list.moves[-1]) == len(
                        self.current_list.moves[-1]
                    ):
                        print("This is the end result already!")
                        return
                    ply = self.grab_move(len_current, 1)
                else:
                    if len(self.current_list.moves[-1]) == 2:
                        ply = self.grab_move(len_current + 1, 0)
                    else:
                        ply = self.grab_move(len_current, 1)
            else:
                ply = self.grab_move(0, 0)
            self.current_list.add_ply(ply)
            print(str(self.current_list))

    def grab_move(self, current, position) -> int:
        """Returns the integer at the given position in history"""
        return self.move_list.moves[current][position]

    def convert_to_matrix(self) -> list[list[str]]:
        """Converts the history to a printable matrix"""
        matrix = []
        for _ in range(self.width):
            matrix.append([])
        for full_move in self.current_list.moves:
            iteration = 0
            for ply in full_move:
                iteration += 1
                if iteration % 2:
                    matrix[ply - 1].append(self.symbol_one)
                else:
                    matrix[ply - 1].append(self.symbol_two)
        for column in matrix:
            fill_column = self.height - len(column)
            for _ in range(fill_column):
                column.append("-")
        return matrix
