"""Testing the Board class for Connect Four game."""
import unittest

from board import Board


def test_board_initialization():
    """Test the initialization of the Board class.

    Feature: The board should have 6 rows and 7 columns

    Scenario: Initialize the board

    Given the game starts and the Board class is initialized
    When the Board class is instantiated
    Then it should create a 6x7 empty grid filled with spaces.
    """
    board = Board()
    assert board.rows == 6
    assert board.columns == 7
    assert all(len(row) == 7 for row in board.grid)
    assert all(cell == " " for row in board.grid for cell in row)


def test_drop_piece_valid():
    """Test dropping a piece into a valid column.

    Feature: Dropping a piece into a column

    Scenario: Drop a piece into a valid column

    Given the game starts and the Board class is initialized
    When a piece is dropped into a valid column
    Then it should be placed in the lowest available row of that column.
    """
    board = Board()
    assert board.drop_piece(0, "X") is True
    assert board.grid[5][0] == "X"


def test_drop_piece_invalid_column():
    """Test dropping a piece into an invalid column.

    Feature: Dropping a piece into a column

    Scenario: Drop a piece into an invalid column

    Given the game starts and the Board class is initialized
    When a piece is dropped into an invalid column (e.g., -1 or 7)
    Then it should return False and not modify the board.
    """
    board = Board()
    assert board.drop_piece(-1, "X") is False
    assert board.drop_piece(7, "X") is False
    assert all(len(row) == 7 for row in board.grid)
    assert all(cell == " " for row in board.grid for cell in row)


def test_drop_piece_full_column():
    """Test dropping a piece into a full column.

    Feature: Dropping a piece into a column

    Scenario: Drop a piece into a full column

    Given during game play, a column is already full
    When a piece is dropped into that column
    Then it should return False and not modify the board.
    """
    board = Board()
    for _ in range(6):
        assert board.drop_piece(0, "X") is True
    assert board.grid[0][0] == "X"
    assert board.drop_piece(0, "O") is False
    assert board.grid[0][0] == "X"


def test_is_full_false():
    """Test if the board is not full.

    Feature: Checking if the board is full

    Scenario: Check if the board is full and it is not

    Given the game starts and the Board class is initialized
    When the board is not full
    Then test if is full should return False.
    """
    board = Board()
    assert board.is_full() is False


def test_is_full_true():
    """Test if the board is full.

    Feature: Checking if the board is full

    Scenario: Check if the board is full and it definitely is

    Given the game starts and the Board class is initialized
    And the board is filled completely
    When the board is full
    Then test if is full should return True.
    """
    board = Board()
    for col in range(board.columns):
        for _ in range(board.rows):
            board.drop_piece(col, "X")
    assert board.is_full() is True


def test_check_winner_horizontal():
    """Test checking for a horizontal winner.

    Feature: Checking for a winner

    Scenario: Check for a horizontal winner

    Given during game play, a player has four pieces in a row horizontally
    When the check_winner method is called
    Then it should return True for that player.
    """
    board = Board()
    for col in range(4):
        board.drop_piece(col, "X")
    assert board.check_winner("X") is True


def test_check_winner_vertical():
    """Test checking for a vertical winner.

    Feature: Checking for a winner

    Scenario: Check for a vertical winner

    Given during game play, a player has four pieces in a row vertically
    When the check_winner method is called
    Then it should return True for that player.
    """
    board = Board()
    for _ in range(4):
        board.drop_piece(0, "X")
    assert board.check_winner("X") is True


def test_check_winner_diagonal_bottom_left_to_top_right():
    """Test checking for a diagonal winner from bottom left to top right.

    Feature: Checking for a winner

    Scenario: Check for a diagonal winner from bottom left to top right

    Given player has 4 pieces in row diagonally from bottom left to top right
    When the check_winner method is called
    Then it should return True for that player.
    """
    board = Board()
    board.drop_piece(0, "X")
    board.drop_piece(1, "O")
    board.drop_piece(1, "X")
    board.drop_piece(2, "O")
    board.drop_piece(2, "O")
    board.drop_piece(2, "X")
    board.drop_piece(3, "O")
    board.drop_piece(3, "O")
    board.drop_piece(3, "O")
    board.drop_piece(3, "X")
    assert board.check_winner("X") is True


def test_check_winner_diagonal_top_left_to_bottom_right():
    """Test checking for a diagonal winner from top left to bottom right.

    Feature: Checking for a winner

    Scenario: Check for a diagonal winner from top left to bottom right

    Given player has 4 pieces in row diagonally from top left to bottom right
    When the check_winner method is called
    Then it should return True for that player.
    """
    board = Board()
    board.drop_piece(3, "X")
    board.drop_piece(2, "O")
    board.drop_piece(2, "X")
    board.drop_piece(1, "O")
    board.drop_piece(1, "O")
    board.drop_piece(1, "X")
    board.drop_piece(0, "O")
    board.drop_piece(0, "O")
    board.drop_piece(0, "O")
    board.drop_piece(0, "X")
    assert board.check_winner("X") is True


def test_check_winner_no_winner():
    """Test checking for no winner.

    Feature: Checking for a winner

    Scenario: Check for no winner

    Given during game play, no player has four pieces in a row
    When the check_winner method is called
    Then it should return False for both players.
    """
    board = Board()
    board.drop_piece(0, "X")
    board.drop_piece(1, "O")
    board.drop_piece(2, "X")
    board.drop_piece(3, "O")
    assert board.check_winner("X") is False
    assert board.check_winner("O") is False


def test_check_is_draw():
    """Test checking for a draw.

    Feature: Checking game result

    Scenario: Check for a draw

    Given during game play, the board is full and no player has won
    When the check_winner method is called
    Then it should return False for both players.
    """
    board = Board()
    for _ in range(3):
        board.drop_piece(0, "X")
        board.drop_piece(1, "O")
        board.drop_piece(2, "X")
        board.drop_piece(3, "X")
        board.drop_piece(4, "X")
        board.drop_piece(5, "O")
        board.drop_piece(6, "X")
        board.drop_piece(0, "O")
        board.drop_piece(1, "X")
        board.drop_piece(2, "O")
        board.drop_piece(3, "O")
        board.drop_piece(4, "O")
        board.drop_piece(5, "X")
        board.drop_piece(6, "O")
    assert board.is_full() is True
    assert board.check_winner("X") is False
    assert board.check_winner("O") is False


def test_reset_board():
    """Test resetting the board.

    Feature: Restart game play

    Scenario: Reset the board

    Given the game play started and the board is filled with some pieces
    When the reset method is called
    Then it should clear the board and set all cells to empty spaces.
    """
    board = Board()
    board.drop_piece(0, "X")
    board.reset()
    assert all(cell == " " for row in board.grid for cell in row)


def test_board_str_empty():
    """Test the string representation of an empty board.

    Feature: Board string representation

    Scenario: Display an empty board

    Given the game starts and the Board class is initialized
    When the __str__ method is called
    Then it should return a string representation of an empty board.
    """
    board = Board()
    expected_output = (
        " | | | | | | \n"
        " | | | | | | \n"
        " | | | | | | \n"
        " | | | | | | \n"
        " | | | | | | \n"
        " | | | | | | \n"
        "-------------\n"
        "0 1 2 3 4 5 6\n"
    )
    assert str(board) == expected_output


def test_board_str_with_pieces():
    """Test the string representation of a board with pieces.

    Feature: Board string representation

    Scenario: Display a board with some pieces

    Given the game is in progress and pieces are dropped into the board
    When the __str__ method is called
    Then it should return a string representation of the board with the pieces.
    """
    board = Board()
    board.drop_piece(0, "X")
    board.drop_piece(1, "O")
    board.drop_piece(1, "X")
    expected_output = (
        " | | | | | | \n"
        " | | | | | | \n"
        " | | | | | | \n"
        " | | | | | | \n"
        " |X| | | | | \n"
        "X|O| | | | | \n"
        "-------------\n"
        "0 1 2 3 4 5 6\n"
    )
    assert str(board) == expected_output


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
