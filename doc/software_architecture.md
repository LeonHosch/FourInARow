# Architecture of a Four in a Row game

We are planning to implement multiple game engines as AI players for the Four in a Row game.

## Board representation

This class shall represent the game Board itself plus it's methods to handle changes applied by a player move.
The Board class also holds the information which of the two players is the currently active player
(So clarifying who's player's turn it is currently).

## Engines

Since there might be multiple Engines implemented this means that there shall be a folder ./engine containing the ai_(engine_type).py files.
Each file represents an own engine type like mcts_uct or minimax or random. As an exceptional game engine there is a human.py
The human.py acts like any other game engine but requests the move to be performed as an user's input entered
on stdin. As an exception the user might enter commands like Take Back, Restart, Change Level, Exit, Redraw, List History

## MoveGenerator

The MoveGenerator is intended to provide a complete list of allowed moves on a given Board.

## History

The History will hold the game history. Mind it should support to Take Back a full move. Mind a full move
consist of two plies. There are plies for one player and the opponent player.
