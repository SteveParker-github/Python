from tkinter import *
from character import Character
from maze import Maze

class Ghost(Character):
    """description of class"""
    #constants
    NROWSCOLUMNS = 21
    NDIRECTIONS = 4
    nextDirection = "left"

    validDirections = [[0, 0],[0, 0],[0, 0],[0, 0]]
    directionNames = ["up", "left", "down", "right"]


    def __init__(self, mazeCanvas, defaultDirection, defaultPosition, name):
        Character.__init__(self, mazeCanvas, defaultDirection, defaultPosition, name)
        self.mazeCanvas = mazeCanvas
        self.WALLS.append("B")

        self.movementOptions = {1: self.GoBack,
                                2: self.OneWay,
                                3: self.Intersection,
                                4: self.Intersection}

        self.images = {"up0": PhotoImage(file = self.IMAGES + "pacman1up.gif"),
                           "up1": PhotoImage(file = self.IMAGES + "pacman2up.gif"),
                           "right0": PhotoImage(file = self.IMAGES + "pacman1right.gif"),
                           "right1": PhotoImage(file = self.IMAGES + "pacman2right.gif"),
                           "down0": PhotoImage(file = self.IMAGES + "pacman1down.gif"),
                           "down1": PhotoImage(file = self.IMAGES + "pacman2down.gif"),
                           "left0": PhotoImage(file = self.IMAGES + "pacman1left.gif"),
                           "left1": PhotoImage(file = self.IMAGES + "pacman2left.gif"),
                           "0": PhotoImage(file = self.IMAGES + "pacman2up1.gif"),
                           "1": PhotoImage(file = self.IMAGES + "pacman2right1.gif"),
                           "2": PhotoImage(file = self.IMAGES + "pacman2down1.gif"),
                           "3": PhotoImage(file = self.IMAGES + "pacman2left1.gif"),
                           "4": PhotoImage(file = self.IMAGES + "pacman2up2.gif"),
                           "5": PhotoImage(file = self.IMAGES + "pacman3up.gif"),
                           "6": PhotoImage(file = self.IMAGES + "pacman4up.gif"),
                           "7": PhotoImage(file = self.IMAGES + "pacman5up.gif"),
                           "8": PhotoImage(file = self.IMAGES + "pacman5up1.gif"),
                           "9": PhotoImage(file = self.IMAGES + "pacman6up.gif")}
        self.ResetPosition()
    
    # checks to see if pacman has eaten either a kibble or the fruit
    def EatItem(self, currentMap, item):
        eatItem = False

        if currentMap[self.GetGridNumber()] == item:
            eatItem = True
        return eatItem

    #finds the position of pacman in the grid
    def GetGridNumber(self):
        gridNumber = int(self.position[1] / self.CELLSIZE) * self.NROWSCOLUMNS + int(self.position[0] / self.CELLSIZE)
        return gridNumber

    def CheckValidMove(self, currentMap):
        validMove = False
        count = 0
        for i in range(self.NDIRECTIONS):
            self.validDirections[i] = self.CheckForWalls(self.directionNames[i], currentMap)
            if self.validDirections[i] != None:
                count += 1
                validMove = True
        self.movementOptions[count](currentMap)

        return validMove

    def GoBack(self, currentMap):
        for i in range(self.NDIRECTIONS):
            if self.validDirections[i] != None:
                self.direction = self.directions[i]

    def OneWay(self, currentMap):
        if self.CheckForWalls(self.direction, currentMap) != None:
            self.position = self.CheckForWalls(self.direction, currentMap)     
        else: #if hit a wall, go the next direction that isnt backtracking
            for i in range(self.NDIRECTIONS):
                if (self.validDirections[i] != None) and (self.direction != self.directionNames[(i + 2)% 4]):
                    self.nextDirection = self.directionNames[i]

            self.direction = self.nextDirection
            self.position = self.CheckForWalls(self.nextDirection, currentMap)

    def Intersection(self, currentMap):
        for i in range(self.NDIRECTIONS):
            if (self.validDirections[i] != None) and (self.direction != self.directionNames[(i + 2)% 4]):
                self.nextDirection = self.directionNames[i]
        self.direction = self.nextDirection
        self.position = self.CheckForWalls(self.nextDirection, currentMap)


    
    