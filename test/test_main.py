"""Unit tests for the four in a row game"""

import unittest

import four_in_a_row


def game_with_matrix(matrix: list[list[str]]) -> four_in_a_row.FourInARow:
    """Creating objects with the given matrix"""
    game: four_in_a_row.FourInARow = four_in_a_row.FourInARow()
    game.load_board(matrix)
    return game


class TestCases(unittest.TestCase):
    """Class used to house the test cases"""

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
            ["X", "-", "-", "-", "-", "-"],
            ["O", "-", "-", "-", "-", "-"],
            ["O", "O", "-", "-", "-", "-"],
            ["O", "X", "O", "-", "-", "-"],
            ["X", "X", "O", "-", "-", "-"],
            ["X", "X", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-"],
        ]
        self.game_one: four_in_a_row.FourInARow = game_with_matrix(matrix_one)
        self.game_two: four_in_a_row.FourInARow = game_with_matrix(matrix_two)

    def test_win(self) -> None:
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
        solution_bool_one: bool = True
        self.assertEqual(self.game_one.win_test([3, 2]), solution_bool_one)

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
        solution_bool_two = False
        self.assertEqual(self.game_two.win_test([5, 1]), solution_bool_two)

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
        solution_int = 2
        self.assertEqual(
            self.game_two.direction_check([-1, 0], "X", [5, 1]), solution_int
        )

    def test_check_finished(self):
        """Testing if check_finished method is working"""
        self.game_one.check_finished()
        self.assertEqual(self.game_one.is_finished, False)

    def test_place_symbol(self):
        """Testing if place_symbol method is working"""
        solution_matrix = [
            ["X", "-", "-", "-", "-", "-"],
            ["O", "-", "-", "-", "-", "-"],
            ["O", "O", "-", "-", "-", "-"],
            ["O", "X", "O", "-", "-", "-"],
            ["X", "X", "O", "O", "-", "-"],
            ["X", "X", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-"],
        ]
        self.game_two.place_symbol(4, "O")
        self.assertEqual(self.game_two.matrix, solution_matrix)


if __name__ == "__main__":
    unittest.main()
