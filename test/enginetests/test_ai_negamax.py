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
        self.board_two: list[list[str]]

    def test_best_play(self):
        """Checking if Negamax returns the best move"""
        negamax_board_one = Negamax(self.board_one, "X", True)
        print(negamax_board_one.best_move)
        self.assertEqual(negamax_board_one.best_move, 3)
