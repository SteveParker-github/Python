from tkinter import *
import os
from maze import Maze

#parent class for pacman and the ghost
class Character():
    #constant
    WALLS = ["n", "e", "w", "s", "N", "E", "W", "S", "^", "<", "V", ">", "|", "-"]
    IMAGES = os.getcwd() + "\\Resources\\Images\\"
    distance = 27
    CELLSIZE = 27
    directions = {"up": [0, -distance],
                  "left": [-distance, 0],
                  "down": [0, distance],
                  "right": [distance, 0]}
    position = [0, 0]
    counter = 0

    #constructor
    def __init__(self, mazeCanvas, defaultDirection, defaultPosition, name):
        self.mazeCanvas = mazeCanvas
        self.defaultDirection = defaultDirection
        self.defaultPosition = defaultPosition
        self.name = name

        self.images = {"pacmanup0": PhotoImage(file = self.IMAGES + "pacman1up.gif"),
                       "pacmanup1": PhotoImage(file = self.IMAGES + "pacman2up.gif"),
                       "pacmanright0": PhotoImage(file = self.IMAGES + "pacman1right.gif"),
                       "pacmanright1": PhotoImage(file = self.IMAGES + "pacman2right.gif"),
                       "pacmandown0": PhotoImage(file = self.IMAGES + "pacman1down.gif"),
                       "pacmandown1": PhotoImage(file = self.IMAGES + "pacman2down.gif"),
                       "pacmanleft0": PhotoImage(file = self.IMAGES + "pacman1left.gif"),
                       "pacmanleft1": PhotoImage(file = self.IMAGES + "pacman2left.gif"),
                       "pacman0": PhotoImage(file = self.IMAGES + "pacman2up1.gif"),
                       "pacman1": PhotoImage(file = self.IMAGES + "pacman2right1.gif"),
                       "pacman2": PhotoImage(file = self.IMAGES + "pacman2down1.gif"),
                       "pacman3": PhotoImage(file = self.IMAGES + "pacman2left1.gif"),
                       "pacman4": PhotoImage(file = self.IMAGES + "pacman2up2.gif"),
                       "pacman5": PhotoImage(file = self.IMAGES + "pacman3up.gif"),
                       "pacman6": PhotoImage(file = self.IMAGES + "pacman4up.gif"),
                       "pacman7": PhotoImage(file = self.IMAGES + "pacman5up.gif"),
                       "pacman8": PhotoImage(file = self.IMAGES + "pacman5up1.gif"),
                       "pacman9": PhotoImage(file = self.IMAGES + "pacman6up.gif"),
                       "blinkyup0": PhotoImage(file = self.IMAGES + "blinky1up.gif"),
                       "blinkyup1": PhotoImage(file = self.IMAGES + "blinky2up.gif"),
                       "blinkyright0": PhotoImage(file = self.IMAGES + "blinky1right.gif"),
                       "blinkyright1": PhotoImage(file = self.IMAGES + "blinky2right.gif"),
                       "blinkydown0": PhotoImage(file = self.IMAGES + "blinky1down.gif"),
                       "blinkydown1": PhotoImage(file = self.IMAGES + "blinky2down.gif"),
                       "blinkyleft0": PhotoImage(file = self.IMAGES + "blinky1left.gif"),
                       "blinkyleft1": PhotoImage(file = self.IMAGES + "blinky2left.gif")}

        self.direction = self.defaultDirection
        self.position = self.defaultPosition

    def CreateImage(self):
        self.imageName = self.name + self.direction + str(self.counter % 2)
        self.mazeCanvas.create_image(self.defaultPosition[0] + (self.CELLSIZE / 2), 
                                     self.defaultPosition[1] + (self.CELLSIZE / 2), 
                                     tags = self.name,
                                     image = self.images[self.imageName])

    #Redraws the character's image on the maze
    def RedrawImage(self):
        self.counter += 1
        self.imageName = self.name + self.direction + str(self.counter % 2)
        self.mazeCanvas.itemconfig(self.name, image = self.images[self.imageName])

    #Places the character into their default position
    def ResetPosition(self):
        self.direction = self.defaultDirection
        self.mazeCanvas.move(self.name,
                             self.defaultPosition[0] - self.position[0], 
                             self.defaultPosition[1] - self.position[1])

        self.position = self.defaultPosition

    #Moves the image based on their direction
    def Move(self, currentMap):
        if self.CheckValidMove(currentMap):
            self.mazeCanvas.move(self.name, 
                                 self.directions[self.direction][0], 
                                 self.directions[self.direction][1])
        self.RedrawImage()

    #checks to see if pacman is able to change direction or continues moving in the same direction
    def CheckValidMove(self, currentMap):
        validMove = False
        tempPosition = self.CheckForWalls(self.nextDirection, currentMap)
        if tempPosition != None:
            self.direction = self.nextDirection
            self.position = tempPosition
            validMove = True
        else:
            tempPosition = self.CheckForWalls(self.direction, currentMap)
            if tempPosition != None:
                self.position = tempPosition
                validMove = True
        return validMove
    
    #checks to see if there is a wall in the direction given
    def CheckForWalls(self, testDirection, currentMap): 
        checkPositions = [self.position[0] + self.directions[testDirection][0],
                          self.position[1] + self.directions[testDirection][1]]
        cellNumber = (int(checkPositions[1] / self.CELLSIZE) * self.NROWSCOLUMNS) + int(checkPositions[0] / self.CELLSIZE)
        if currentMap[cellNumber] in self.WALLS:
            checkPositions = None
        return checkPositions


    #finds the position of the character in the grid
    def GetGridNumber(self):
        gridNumber = int(self.position[1] / self.CELLSIZE) * self.NROWSCOLUMNS + int(self.position[0] / self.CELLSIZE)
        return gridNumber
