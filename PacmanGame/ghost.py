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
        self.WALLS.append("B")

        self.movementOptions = {1: self.GoBack,
                                2: self.OneWay,
                                3: self.Intersection,
                                4: self.Intersection}

    

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

    def CheckPacmanRange(self, currentMap):
        chaseMode = false
        distance = 0

    def ChasePacman(self, currentMap):
          chase = false