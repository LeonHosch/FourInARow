"""Game history management

The history module provides functionality to manage the history of moves
in a Connect Four game.

Like in computer chess programming the history class is storing sets of
so called Plies (single: Ply) representing a player's move.
A Ply denotes a half-move performed by one player and in that case
represents the column index where the player dropped a piece.

Thus a full-move is represented by two Ply objects, one for each player.
The history class provides methods to add a Ply, undo the last full-move.

A readable string representation of the history is also provided and
typically looks like this:

1. [3, 4] 2. [3, 5] 3. [4, 5] 4. [2, 2] 5. [1, 1] 6. [0, 0]
7. [0, 1] 8. [1, 2] 9. [2, 3] 10. [3, 4] 11. [4, 5] 12. [5, 6]

meaning that in the first full-move the first player dropped a
piece in column 3, the second player in column 4,
then in second full-move the first player in column 3 again, followed by
the second player in column 5 again and so on.
"""

from typing import List


class History:
    """Class to manage game history"""
    def __init__(self) -> None:
        """Initialize the history list"""
        self.moves: List[List[int]] = []

    def add_ply(self, column: int) -> None:
        """Add a Ply (a single half-move) to the history

        :param column: The column index where the piece was dropped."""
        if not self.moves or len(self.moves[-1]) == 2:
            self.moves.append([column])
        else:
            self.moves[-1].append(column)

    def undo_last_full_move(self) -> None:
        """Undo the last full-move (two Plies)"""
        if self.moves:
            if len(self.moves[-1]) == 2:
                self.moves.pop()
            elif len(self.moves[-1]) == 1:
                self.moves.pop()

    def __str__(self) -> str:
        """Return a readable string representation of the history"""
        return " ".join(f"{i + 1}. {move}"
                        for i, move in enumerate(self.moves))
