"""Used for testing the functionality of ai_negamax.py"""

import unittest

from engine.ai_negamax_2 import Negamax


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
        negamax_board_one = Negamax(self.board_one, "X")
        # print(negamax_board_one.best_move)
        self.assertEqual(negamax_board_one.best_move, 3)

    def test_best_play_two(self):
        """Checking if Negamax returns the best move"""
        negamax_board_two = Negamax(self.board_two, "X")
        self.assertEqual(negamax_board_two.best_move, 3)
