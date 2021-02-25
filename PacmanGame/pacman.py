from tkinter import *
from character import Character

class Pacman(Character):
    """description of class"""
    #constants
    NROWSCOLUMNS = 21
    
    nextDirection = "right"
    

    def __init__(self, mazeCanvas, defaultDirection, defaultPosition, name):
        Character.__init__(self, mazeCanvas, defaultDirection, defaultPosition, name)
        self.WALLS.append("B")

    # checks to see if pacman has eaten either a kibble or the fruit
    def EatItem(self, currentMap, item):
        eatItem = False

        if currentMap[self.GetGridNumber()] == item:
            eatItem = True
        return eatItem
    
    