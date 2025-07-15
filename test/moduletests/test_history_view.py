"""Used for testing the functionality of the history_view class"""

import unittest

from modules.history_view import ViewHistory
from modules.history import History


class TestCases(unittest.TestCase):
    """Contains methods used for testing the history_view class"""

    def setUp(self):
        history_one = History()
        history_one.moves = [
            [4, 2],
            [3, 2],
            [6, 5],
            [4, 3],
            [5, 4],
            [6, 3],
            [5, 6],
            [6],
        ]
        self.history_one: ViewHistory = ViewHistory(history_one, 7, 6, "O")

    def test_move_back(self):
        """Testing if you can undo a move in history_view"""
        solution_list: list[list[int]] = [
            [4, 2],
            [3, 2],
            [6, 5],
            [4, 3],
            [5, 4],
            [6, 3],
            [5, 6],
        ]
        self.history_one.move_back()
        self.assertEqual(self.history_one.current_list.moves, solution_list)

    def test_move_forward(self):
        """Testing if you can redo a move in history_view"""
        solution_list: list[list[int]] = [
            [4, 2],
            [3, 2],
            [6, 5],
            [4, 3],
            [5, 4],
            [6, 3],
            [5, 6],
            [6],
        ]
        self.history_one.move_forward()
        self.assertEqual(self.history_one.current_list.moves, solution_list)

    def test_grab_move(self):
        """Testing if the grab_move method works correctly"""
        solution_int: int = 6
        self.assertEqual(self.history_one.grab_move(2, 0), solution_int)

    def test_convert_to_matrix(self):
        """Testing if you can convert the move list to a printable matrix"""
        solution_matrix = [
            ["-", "-", "-", "-", "-", "-"],
            ["X", "X", "-", "-", "-", "-"],
            ["O", "X", "X", "-", "-", "-"],
            ["O", "O", "X", "-", "-", "-"],
            ["X", "O", "O", "-", "-", "-"],
            ["O", "O", "X", "O", "-", "-"],
            ["-", "-", "-", "-", "-", "-"],
        ]
        self.assertEqual(self.history_one.convert_to_matrix(), solution_matrix)
