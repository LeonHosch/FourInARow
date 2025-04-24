"""Unit tests for the four in a row game"""

import unittest

import four_in_a_row


def game_with_matrix(matrix: list[list[str]]) -> four_in_a_row.FourInARow:
    """Creating objects with the given matrix"""
    game = four_in_a_row.FourInARow()
    game.load_board(matrix)
    return game


class TestCases(unittest.TestCase):
    """Class used to house the test cases"""

    def setUp(self):  # pylint: disable=invalid-name
        matrix_one = [
            ["-", "-", "-", "-", "-", "-"],
            ["O", "X", "-", "-", "-", "-"],
            ["O", "O", "-", "-", "-", "-"],
            ["O", "X", "O", "-", "-", "-"],
            ["X", "X", "X", "O", "-", "-"],
            ["X", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-"],
        ]
        matrix_two = [
            ["-", "-", "-", "-", "-", "-"],
            ["O", "X", "-", "-", "-", "-"],
            ["O", "O", "-", "-", "-", "-"],
            ["O", "X", "O", "-", "-", "-"],
            ["X", "X", "O", "-", "-", "-"],
            ["X", "X", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-"],
        ]
        self.game_one = game_with_matrix(matrix_one)
        self.game_two = game_with_matrix(matrix_two)

    def test_win(self):
        """Test if the given gameboard with given input is won or not"""
        # Given:    A gameboard in following state:
        #            -----------------------
        #           |  -  -  -  -  -  -  -  |
        #           |  -  -  -  -  -  -  -  |
        #           |  -  -  -  -  O  -  -  |
        #           |  -  -  -  O  X  -  -  |
        #           |  -  X  O  X  X  -  -  |
        #           |  -  O  O  O  X  X  -  |
        #            -----------------------
        # When:     Gameboard is checked at coordinates [3, 2] using the win_test() method
        # Then:     True should be returned, which will end the game and
        #           notify the player O that he has won
        game_one_outcome = True
        self.assertEqual(game_one_outcome, self.game_one.win_test([3, 2]))

        # Given:    A gameboard in following state:
        #            -----------------------
        #           |  -  -  -  -  -  -  -  |
        #           |  -  -  -  -  -  -  -  |
        #           |  -  -  -  -  -  -  -  |
        #           |  -  -  -  O  O  -  -  |
        #           |  -  X  O  X  X  X  -  |
        #           |  -  O  O  O  X  X  -  |
        #            -----------------------
        # When:     Gameboard is checked at coordinates [5, 1] using the win_test method
        # Then:     False should be returned and the game will keep going as no one has won yet
        game_two_outcome = False
        self.assertEqual(game_two_outcome, self.game_two.win_test([5, 1]))

    def test_direction_check(self):
        """Test the direction_check method of the Four in a row game"""
        # Given:    The direction [-1, 0], the symbol 'X' and the coordinates
        #           [5, 1] on a gameboard that looks like this:
        #            -----------------------
        #           |  -  -  -  -  -  -  -  |
        #           |  -  -  -  -  -  -  -  |
        #           |  -  -  -  -  -  -  -  |
        #           |  -  -  -  O  O  -  -  |
        #           |  -  X  O  X  X  X  -  |
        #           |  -  O  O  O  X  X  -  |
        #            -----------------------
        # When:     Method direction_check is called with the prior mentioned parameters
        # Then:     The number 2 should be returned, as the coordinate has 2 matching
        #           symbols in a row in the given direction
        expected_result = 2
        self.assertEqual(
            expected_result, self.game_two.direction_check([-1, 0], "X", [5, 1])
        )


if __name__ == "__main__":
    unittest.main()
