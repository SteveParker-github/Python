from tkinter import *
from character import Character

import os

class Pacman(Character):
    """description of class"""
    #constants
    CELLSIZE = 27
    PACMANX = 10 * CELLSIZE
    PACMANY = 15 * CELLSIZE
    IMAGES = os.getcwd() + "\\Resources\\Images\\"

    def __init__(self, mazeCanvas):
        self.mazeCanvas = mazeCanvas
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
        self.pacmanImage = self.mazeCanvas.create_image(self.PACMANX + (self.CELLSIZE / 2) , 
                                     self.PACMANY + (self.CELLSIZE / 2), 
                                     image = self.pacmanType[self.imageName])

    def MoveImage(self):
        self.counter += 1
        self.imageName = self.direction + str(self.counter % 2)
        self.mazeCanvas.itemconfig(self.pacmanImage, image = self.pacmanType[self.imageName])
        self.mazeCanvas.move(self.pacmanImage, self.directions[self.direction][0], self.directions[self.direction][1])

    
    