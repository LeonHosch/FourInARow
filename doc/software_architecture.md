# Software Architecture of the Four in a Row Game

This document outlines the architecture for implementing a Four in a Row game,
including its components and their responsibilities.

## Overview

The game will support multiple AI engines as players, alongside a human player.
This modular architecture ensures flexibility, scalability, and ease of maintenance for the Four in a Row game.

## Board Representation

The `Board` class represents the game board and provides methods to manage player moves.
It also tracks the currently active player, ensuring clarity on whose turn it is.

### Responsibilities

- **State Management**: Maintain the board state and the active player.
- **Winning Condition Check**: Provide a method to check if the game has ended. This method returns a tuple `(end_of_game: bool, winner: Optional[symbol])`, where `winner` is the symbol of the winning player or `None` if there is no winner.
- **Undo Functionality**: Implement an `undo_ply` method to revert the last half move (aka ply like in computer chess (one ply, multiple plies)).

## Game Engines

The game supports multiple AI engines, each implemented as a separate module in the `./engine` folder. Each engine is responsible for determining the next move based on its algorithm.

### Engine Types

- **AI Engines**: Examples include `ai_mcts_uct.py`, `ai_minimax.py`, `ai_neural_network.py`, `ai_zero_alpha.py`, and `ai_random.py`.
- **Human Engine**: The `human.py` module acts as a game engine but interacts with the user via standard input. It also supports commands such as:
  - `Take Back` or `Undo`
  - `Restart`
  - `Change Level`
  - `Switch Engine`
  - `Exit`
  - `Redraw`
  - `List History`

## Move Generator

The `MoveGenerator` class provides a complete list of valid moves for a given board state. This ensures that all engines and the human player operate within the game's rules.

## Game History

The `History` class maintains a record of all moves made during the game. It supports:

- **Undo Functionality**: Allowing the reversal of a full move (two plies) or a single ply.
- **Move Tracking**: Storing the sequence of moves for replay or analysis.
- **Replay Functionality**: Provide an iterator or pointer in the game's History to traverse or play back single moves step by step.

### Terminology

- **Ply**: A single move by one player.
- **Full Move**: A pair of plies, one from each player.
