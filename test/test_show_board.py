"""Used for testing if the show_board class is working"""

import unittest

from modules.show_board import ShowBoard


class TestCases(unittest.TestCase):
    """Used for testing the methods in ShowBoard"""

    def setUp(self) -> None:
        matrix_one: list[list[str]] = [
            ["-", "-", "-", "-", "-", "-"],
            ["O", "X", "-", "-", "-", "-"],
            ["O", "O", "-", "-", "-", "-"],
            ["O", "X", "O", "-", "-", "-"],
            ["X", "X", "X", "O", "-", "-"],
            ["X", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-"],
        ]
        matrix_two: list[list[str]] = [
            ["X", "X", "O", "X", "X"],
            ["O", "X", "O", "O", "O"],
            ["O", "O", "O", "X", "O"],
            ["O", "X", "X", "O", "O"],
            ["X", "O", "X", "O", "X"],
            ["X", "O", "x", "X", "X"],
            ["O", "X", "O", "O", "O"],
            ["X", "X", "O", "O", "-"],
            ["O", "X", "O", "-", "-"],
        ]
        self.board_one = ShowBoard(matrix_one, 7, 6)
        self.board_two = ShowBoard(matrix_two, 9, 5)

    def test_calculate_breaker(self) -> None:
        """Testing if the breaker string is calculated correctly"""
        solution_str_one: str = " -----------------------"
        solution_str_two: str = " -----------------------------"
        self.assertEqual(self.board_one.calculate_breaker(), solution_str_one)
        self.assertEqual(self.board_two.calculate_breaker(), solution_str_two)
