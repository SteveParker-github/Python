from tkinter import *
import random
import os
from PIL import Image

class Fruit():
    """description of class"""
    DEFAULTTIMER = 30
    MINKIBBLES = 100
    CHANCE = 40
    NROWSCOLUMNS = 21
    CELLSIZE = 27
    MAXSWAPS = 20
    IMAGES = os.getcwd() + "\\Resources\\Images\\"
    active = False
    validLocations = []
    fruitLocation = None
    timer = 0

    def __init__(self, mazeCanvas):
        self.mazeCanvas = mazeCanvas
        self.fruitImages = [PhotoImage(file = self.IMAGES + "Fruit.gif")] #will expand this to have multiple images

    #runs the fruit and see what it needs to do
    def Run(self, currentMap, nKibbles):
        newFruit = False
        if self.active:
            self.timer -= 1
            if self.timer == 0:
                self.RemoveFruit()
        else:
            if int(nKibbles) < self.MINKIBBLES and random.randrange(self.CHANCE) == 0: 
                self.CreateFruit(currentMap)
                newFruit = True
        return newFruit

    #create a fruit on the maze
    def CreateFruit(self, currentMap):
        self.timer = self.DEFAULTTIMER
        self.FindLocation(currentMap)
        location = random.randrange(len(self.validLocations))
        self.fruitLocation = self.validLocations[location]
        self.mazeCanvas.create_image(int(self.fruitLocation % self.NROWSCOLUMNS) * self.CELLSIZE + (self.CELLSIZE / 2), 
                                     int(self.fruitLocation / self.NROWSCOLUMNS) * self.CELLSIZE + (self.CELLSIZE / 2), 
                                      image = self.fruitImages[random.randrange(len(self.fruitImages))],
                                      tags = "Fruit")
        self.active = True

    #find available locations the fruit can be placed
    def FindLocation(self, currentMap):
        for i in range(len(currentMap)):
            if currentMap[i] == "f":
                self.validLocations.append(i)

    #remove the fruit from the map 
    def RemoveFruit(self):
        self.active = False
        self.mazeCanvas.delete("Fruit")
        

