"""An AI player, that plays random moves"""

import random


class Random:
    """The class for the random AI player"""

    def __init__(self, gamestate, symbol, boardsize) -> None:
        """Initializing the class for the needed parameters"""
        self.gamestate = gamestate
        self.points = 0
        self.symbol = symbol
        self.height = boardsize[0]
        self.width = boardsize[1]
        self.random_move = self.bot_random()

    def bot_random(self) -> int:
        """the AI of the bot player"""
        while True:
            move = random.randint(0, self.width)
            if len(self.gamestate[move]) < self.height:
                return move
