"""Used for testing the functionality of ai_negamax.py"""

import unittest

from engine.ai_negamax import Negamax


class TestCases(unittest.TestCase):
    """Contains the methods used for testing"""

    def setUp(self):  # pylint: disable=invalid-name
        self.board_one: list[list[str]] = [
            ["X", "X", "O", "X", "X", "X"],
            ["O", "X", "O", "O", "O", "X"],
            ["O", "O", "O", "X", "O", "X"],
            ["O", "X", "X", "O", "O", "-"],
            ["X", "O", "X", "O", "X", "-"],
            ["X", "O", "x", "X", "X", "O"],
            ["O", "X", "O", "O", "O", "-"],
        ]
        self.board_two: list[list[str]] = [
            ["X", "X", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-"],
            ["O", "O", "O", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-"],
        ]

    def test_best_play_one(self):
        """Checking if Negamax returns the best move"""
        solution_int: int = 3
        negamax_board_one: Negamax = Negamax(self.board_one, "X")
        self.assertEqual(negamax_board_one.best_move, solution_int)

    def test_best_play_two(self):
        """Checking if Negamax returns the best move"""
        solution_int: int = 3
        negamax_board_two: Negamax = Negamax(self.board_two, "X")
        self.assertEqual(negamax_board_two.best_move, solution_int)

    def test_horizontal_points(self):
        """Checking if the foreseen number of points are assigned to the gamefield"""
        solution_int_one: int = 8
        solution_int_two: int = 14
        solution_int_three: int = 0
        solution_int_four: int = 0
        gamestate_one: Negamax = Negamax(self.board_one, "X")
        gamestate_two: Negamax = Negamax(self.board_one, "O")
        gamestate_three: Negamax = Negamax(self.board_two, "X")
        gamestate_four: Negamax = Negamax(self.board_two, "O")
        self.assertEqual(gamestate_one.check_horizontal(), solution_int_one)
        self.assertEqual(gamestate_two.check_horizontal(), solution_int_two)
        self.assertEqual(gamestate_three.check_horizontal(), solution_int_three)
        self.assertEqual(gamestate_four.check_horizontal(), solution_int_four)

    def test_vertical_points(self):
        """Checking if the foreseen number of points are assigned to the gamefield"""
        solution_int_one: int = 4
        solution_int_two: int = 5
        solution_int_three: int = 1
        solution_int_four: int = 4
        gamestate_one: Negamax = Negamax(self.board_one, "X")
        gamestate_two: Negamax = Negamax(self.board_one, "O")
        gamestate_three: Negamax = Negamax(self.board_two, "X")
        gamestate_four: Negamax = Negamax(self.board_two, "O")
        self.assertEqual(gamestate_one.check_vertical(), solution_int_one)
        self.assertEqual(gamestate_two.check_vertical(), solution_int_two)
        self.assertEqual(gamestate_three.check_vertical(), solution_int_three)
        self.assertEqual(gamestate_four.check_vertical(), solution_int_four)

    def test_set_opposite(self):
        """Testing the set_opposite method of the negamax ai player"""
        gamestate_one: Negamax = Negamax(self.board_one, "X")
        gamestate_two: Negamax = Negamax(self.board_one, "O")
        solution_str_one: str = "O"
        solution_str_two: str = "X"
        gamestate_one.opposite_symbol = "X"
        gamestate_two.opposite_symbol = "O"
        gamestate_one.set_opposite()
        gamestate_two.set_opposite()
        self.assertEqual(gamestate_one.opposite_symbol, solution_str_one)
        self.assertEqual(gamestate_two.opposite_symbol, solution_str_two)
