import random

def intsafeinput(text):
    while True:
        try:
            integer = int(input(text))
            return integer
        except:
            print("Integer input expected\n")

class FourInARow:

    # initializing the game class
    def __init__(self):
        self.matrix = [[], [], [], [], [], [], []]
        self.width = len(self.matrix)
        self.height = 6
        self.printplayfield()
        self.gameplay()
        return

    # prints the matrix so the player can see what the playfield looks like
    # with the current moves shown on the board
    def printplayfield(self):
        print(" -----------------------")
        for x_coordinate in range(self.height-1, -1, -1):
            print("|", end="  ")
            for entry in self.matrix:
                try:
                    print(entry[x_coordinate], end="  ")
                except:
                    print("-", end="  ")
            print("|")
        print(" -----------------------")
        return

    # gameplay loop of our connect-four game
    def gameplay(self):
        maxmoves = self.width * self.height
        for counter in range(maxmoves):
            if counter % 2:
                symbol = "X"
                column = self.bot_play()
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
                        else:
                            print("Column is filled already!\n")
                    except:
                        print(f"There are only {self.width} columns!\n")

            self.matrix[column].append(symbol)
            self.printplayfield()
            if self.win_test([column, len(self.matrix[column])-1], symbol):
                print(f"The player with the symbol '{symbol}' won the game!")
                return

    # check if the game has been won by adding up matching symbols in a row
    def win_test(self, coordinates, symbol):
        directions = [(-1, 0), (1, 0), (-1, -1), (1, 1), (1, -1), (-1, 1), (0, -1)]
        counter = 0
        previous = 0
        for direction in directions:
            symbol_in_row = self.direction_check(direction, symbol, [coordinates[0], coordinates[1]])
            if symbol_in_row + previous >= 3:
                return True
            if counter % 2:
                previous = 0
            else:
                previous = symbol_in_row
            counter += 1
        return False

    # check the given direction for matching symbols
    def direction_check(self, direction, symbol, coordinates):
        erg = 0
        while True:
            coordinates[0] += direction[0]
            coordinates[1] += direction[1]
            y_height = len(self.matrix[coordinates[0]])
            if self.width > coordinates[0] >= 0 and y_height > coordinates[1] >= 0:
                if self.matrix[coordinates[0]][coordinates[1]] == symbol:
                    erg += 1
                else:
                    return erg
            else:
                return erg

    # the AI of the bot player
    def bot_play(self):
        while True:
            move = random.randint(0, 6)
            if len(self.matrix[move]) < self.height:
                return move


game = FourInARow()
print("Thanks for playing!")