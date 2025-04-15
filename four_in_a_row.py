""" A simple console-based Connect Four game in Python """

import random
from engine import bot_minimax
from copy import deepcopy

def intsafeinput(text):
    """ function which is used to safely get an integer input"""
    while True:
        try:
            integer = int(input(text))
            return integer
        except ValueError:
            print("Integer input expected\n")

class FourInARow:
    """ The game class containing the methods needed to run the game """

    def __init__(self, matrix = None):
        """ initializing the game class """
        if matrix is None:
            self.matrix = [[], [], [], [], [], [], []]
        else:
            self.matrix = matrix
        self.width = len(self.matrix)
        self.height = 6
        self.print_playfield()

    def print_playfield(self):
        """ prints the matrix so the player can see what the playfield looks like
        with the current moves shown on the board """
        print(" -----------------------")
        for x_coordinate in range(self.height-1, -1, -1):
            print("|", end="  ")
            for entry in self.matrix:
                try:
                    print(entry[x_coordinate], end="  ")
                except IndexError:
                    print("-", end="  ")
            print("|")
        print("| --------------------- |")
        print("|  1  2  3  4  5  6  7  |")
        print(" -----------------------")

    def gameplay(self):
        """ gameplay loop of our connect-four game """
        maxmoves = self.width * self.height
        for counter in range(maxmoves):
            if counter % 2:
                symbol = "X"
                gamestate = deepcopy(self.matrix)
                minimax = bot_minimax.Minimax(gamestate, symbol, self.height, self.width)
                column = minimax.best_move
                self.print_playfield()
                if len(self.matrix[column]) >= self.height:
                    print("Bot played an illegal move!")
                # column = self.bot_play()
            else:
                symbol = "O"

                print(f"Where do you want to put an {symbol}?")

                while True:
                    column = intsafeinput(f"Choose column from 1 to {self.width}: ") - 1
                    if column == -1:
                        return
                    try:
                        if len(self.matrix[column]) < self.height:
                            break
                        print("Column is filled already!\n")
                    except IndexError:
                        print(f"There are only {self.width} columns!\n")

            self.matrix[column].append(symbol)
            self.print_playfield()
            print(self.matrix)
            if self.win_test([column, len(self.matrix[column])-1], symbol):
                print(f"The player with the symbol '{symbol}' won the game!")
                return

    def win_test(self, coordinates, symbol):
        """ check if the game has been won by adding up matching symbols in a row """
        directions = [(-1, 0), (1, 0), (-1, -1), (1, 1), (1, -1), (-1, 1), (0, -1)]
        counter = 0
        previous = 0
        for direction in directions:
            win_con = self.direction_check(direction, symbol, [coordinates[0], coordinates[1]]) # review!
            if win_con + previous >= 3:
                return True
            if counter % 2:
                previous = 0
            else:
                previous = win_con
            counter += 1
        return False

    def direction_check(self, direction, symbol, coordinates):
        """ check the given direction for matching symbols """
        result = 0
        while True:
            coordinates[0] += direction[0]
            coordinates[1] += direction[1]
            if self.width > coordinates[0] >= 0:
                if len(self.matrix[coordinates[0]]) > coordinates[1] >= 0:
                    if self.matrix[coordinates[0]][coordinates[1]] == symbol:
                        result += 1
                    else:
                        return result
                else:
                    return result
            else:
                return result

    def bot_play(self):
        """ the AI of the bot player """
        while True:
            move = random.randint(0, 6)
            if len(self.matrix[move]) < self.height:
                return move

if __name__ == "__main__":
    game = FourInARow()
    game.gameplay()
    print("Thanks for playing!")
