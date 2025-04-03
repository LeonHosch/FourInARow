import random

def intsafeinput(text):
    while True:
        try:
            integer = int(input(text))
            return integer
        except:
            print("Integer input expected\n")

class fourInARow:
    
    def __init__(self):
        self.matrix = [[], [], [], [], [], [], []]
        self.width = len(self.matrix)
        self.height = 6
        self.printplayfield()
        self.gameplay()
        return
    
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
    
    def gameplay(self):
        maxmoves = self.width * self.height
        for counter in range(maxmoves):
            if counter % 2:
                symbol = "X"
                column = self.botPlay()
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
            if self.betterWinTest([column, len(self.matrix[column])-1], symbol):
                print(f"The player with the symbol '{symbol}' won the game!")
                return

    def betterWinTest(self, coordinates, symbol):
        directions = [(-1, 0), (1, 0), (-1, -1), (1, 1), (1, -1), (-1, 1), (0, -1)]
        counter = 0
        previous = 0
        for direction in directions:
            symbol_in_row = self.betterDirectionCheck(direction, symbol, [coordinates[0], coordinates[1]])
            if symbol_in_row + previous >= 3:
                return True
            elif counter % 2:
                previous = 0
            else:
                previous = symbol_in_row
            counter += 1
        return False
    
    def betterDirectionCheck(self, direction, symbol, coordinates):
        erg = 0
        while True:
            coordinates[0] += direction[0]
            coordinates[1] += direction[1]
            if self.width > coordinates[0] >= 0 and len(self.matrix[coordinates[0]]) > coordinates[1] >= 0:
                if self.matrix[coordinates[0]][coordinates[1]] == symbol:
                    erg += 1
                else:
                    return erg
            else:
                return erg
            
    def botPlay(self):
        while True:
            move = random.randint(0, 6)
            if len(self.matrix[move]) < self.height:
                return move

    # def winTest(self, coordinates, symbol):
    #     return_left_down = 0
    #     return_right_up = 0
    #     return_right_down = 0
    #     return_left_up = 0
    #     return_left = 0
    #     return_right = 0
    #     return_down = 0

    #     if coordinates[0] - 1 >= 0 and coordinates[1] - 1 >= 0:
    #         return_left_down = self.directionCheck((-1, -1), symbol, [coordinates[0]-1, coordinates[1]-1])
    #         if return_left_down >= 3:
    #             return True
    #     if coordinates[0] +1 <= self.width and coordinates[1] + 1 <= self.height:
    #         return_right_up = self.directionCheck((1, 1), symbol, [coordinates[0]+1, coordinates[1]+1])
    #         if return_right_up >= 3:
    #             return True
    #     if return_left_down + return_right_up >= 3:
    #         return True
    #     if coordinates[0] - 1 >=0 and coordinates[1] + 1 <= self.height:
    #         return_right_down = self.directionCheck((-1, 1), symbol, [coordinates[0]-1, coordinates[1]+1])
    #         if return_right_down >= 3:
    #             return True
    #     if coordinates[0] + 1 <= self.width and coordinates[1] - 1 <= self.height:
    #         return_left_up = self.directionCheck((1, -1), symbol, [coordinates[0]+1, coordinates[1]-1])
    #         if return_left_up >= 3:
    #             return True
    #     if return_right_down + return_left_up >= 3:
    #         return True
    #     if coordinates[0] -1 >=0:
    #         return_left = self.directionCheck((-1, 0), symbol, [coordinates[0]-1, coordinates[1]])
    #         if return_left >= 3:
    #             return True
    #     if coordinates[0] +1 <= self.width:
    #         return_right = self.directionCheck((1, 0), symbol, [coordinates[0]+1, coordinates[1]])
    #         if return_right >= 3:
    #             return True
    #     if return_left + return_right >= 3:
    #         return True
    #     if coordinates[1] - 1 >= 0:
    #         return_down = self.directionCheck((0, -1), symbol, [coordinates[0], coordinates[1]-1])
    #         if return_down >= 3:
    #             return True
    #     return False

    # def directionCheck(self, direction, symbol, coordinates):
    #     try:
    #         if self.matrix[coordinates[0]][coordinates[1]] == symbol:
    #             if coordinates[0] + direction[0] >= 0 and coordinates[1] + direction[1] >= 0:
    #                 return self.directionCheck(direction, symbol, [coordinates[0]+direction[0], coordinates[1]+direction[1]]) + 1
    #             else:
    #                 return 1
    #         return 0
    #     except:
    #         return 0


game = fourInARow()
print("Thanks for playing!")