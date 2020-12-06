from tkinter import *
from character import Character
from maze import Maze

import os

class Pacman(Character):
    """description of class"""
    #constants
    CELLSIZE = 27
    PACMANX = 10 * CELLSIZE
    PACMANY = 15 * CELLSIZE
    NROWSCOLUMNS = 21
    IMAGES = os.getcwd() + "\\Resources\\Images\\"

    nextDirection = "right"

    def __init__(self, mazeCanvas):
        self.mazeCanvas = mazeCanvas
        self.WALLS.append("B")

        self.pacmanType = {"up0": PhotoImage(file = self.IMAGES + "pacman1up.gif"),
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
        self.counter = 0
        self.imageName = self.direction + str(self.counter % 2)
        self.pacmanImage = self.mazeCanvas.create_image(self.PACMANX + (self.CELLSIZE / 2), 
                                                        self.PACMANY + (self.CELLSIZE / 2), 
                                                        image = self.pacmanType[self.imageName])
        self.position = [self.PACMANX, self.PACMANY]

    def MoveImage(self):
        self.mazeCanvas.move(self.pacmanImage, 
                             self.directions[self.direction][0], 
                             self.directions[self.direction][1])

    def RedrawImage(self):
        self.counter += 1
        self.imageName = self.direction + str(self.counter % 2)
        self.mazeCanvas.itemconfig(self.pacmanImage, image = self.pacmanType[self.imageName]) #by having a tag on the image we can move this into the parent

    def CheckNoWall(self, currentMap):
        if self.CheckForWalls(self.nextDirection, currentMap) != None:
            self.direction = self.nextDirection
            self.position = self.CheckForWalls(self.nextDirection, currentMap)
            self.MoveImage()
        else:
            if self.CheckForWalls(self.direction, currentMap) != None:
                self.position = self.CheckForWalls(self.direction, currentMap)
                self.MoveImage()

    def CheckForWalls(self, testDirection, currentMap):          
        checkPositions = [self.position[0] + self.directions[testDirection][0],
                          self.position[1] + self.directions[testDirection][1]]
        cellNumber = (int(checkPositions[1] / self.CELLSIZE) * self.NROWSCOLUMNS) + int(checkPositions[0] / self.CELLSIZE)
        if currentMap[cellNumber] in self.WALLS:
            checkPositions = None
        return checkPositions

    def EatKibble(self, currentMap):
        eatKibble = False

        if currentMap[self.GetGridNumber()] == "k":
            eatKibble = True

        return eatKibble

    def GetGridNumber(self):
        cellNumber = int(self.position[1] / self.CELLSIZE) * self.NROWSCOLUMNS + int(self.position[0] / self.CELLSIZE)
        return cellNumber
    
    