"""Test cases for the History class in game history management."""
import unittest

from history import History


class TestHistory(unittest.TestCase):
    """Test cases for the History class"""

    def setUp(self):
        """Set up a new history instance before each test"""
        self.history = History()

    def test_add_ply_single(self):
        """Test adding a single ply"""
        self.history.add_ply(3)
        self.assertEqual(self.history.moves, [[3]])

    def test_add_ply_multiple(self):
        """Test adding multiple plies"""
        self.history.add_ply(3)
        self.history.add_ply(4)
        self.history.add_ply(5)
        self.assertEqual(self.history.moves, [[3, 4], [5]])

    def test_undo_last_full_move_single(self):
        """Test undoing the last full move with a single ply"""
        self.history.add_ply(3)
        self.history.undo_last_full_move()
        self.assertEqual(self.history.moves, [])

    def test_undo_last_full_move_multiple(self):
        """Test undoing the last full move with multiple plies"""
        self.history.add_ply(3)
        self.history.add_ply(4)
        self.history.add_ply(5)
        self.history.add_ply(6)
        self.history.undo_last_full_move()
        self.assertEqual(self.history.moves, [[3, 4]])

    def test_undo_last_full_move_empty(self):
        """Test undoing the last full move when history is empty"""
        self.history.undo_last_full_move()
        self.assertEqual(self.history.moves, [])

    def test_str_representation_empty(self):
        """Test string representation of an empty history"""
        self.assertEqual(str(self.history), "")

    def test_str_representation_non_empty(self):
        """Test string representation of a non-empty history"""
        self.history.add_ply(3)
        self.history.add_ply(4)
        self.history.add_ply(5)
        self.assertEqual(str(self.history), "1. [3, 4] 2. [5]")


if __name__ == "__main__":
    unittest.main()
