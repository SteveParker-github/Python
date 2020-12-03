from tkinter import *
import os

class Maze():
    """description of class"""
    #constants
    NROWSCOLUMNS = 21
    CELLSIZE = 27
    #SPACESIZE = 1
    TOTALCELLS = NROWSCOLUMNS * NROWSCOLUMNS
    IMAGES = os.getcwd() + "\\Resources\\Images\\"

    startMap = "bwwwwwwwwwwwwwwwwwwwb" + \
           "bwkkkkkkkkwkkkkkkkkwb" + \
           "bwkwwkwwwkwkwwwkwwkwb" + \
           "bwkkkkkkkkkkkkkkkkkwb" + \
           "bwkwwkwkwwwwwkwkwwkwb" + \
           "bwkkkkwkkkwkkkwkkkkwb" + \
           "bwwwwkwwwbwbwwwkwwwwb" + \
           "bbbbwkwbbbbbbbwkwbbbb" + \
           "wwwwwkwbwwbwwbwkwwwww" + \
           "bbbbwkbbwbbbwbbkwbbbb" + \
           "wwwwwkwbwwwwwbwkwwwww" + \
           "bbbbwkwbbbbbbbwkwbbbb" + \
           "bwwwwkwbwwwwwbwkwwwwb" + \
           "bwkkkkkkkkwkkkkkkkkwb" + \
           "bwkwwkwwwkwkwwwkwwkwb" + \
           "bwkkwkkkkkbkkkkkwkkwb" + \
           "bwwkwkwkwwwwwkwkwkwwb" + \
           "bwkkkkwkkkwkkkwkkkkwb" + \
           "bwkwwwwwwkwkwwwwwwkwb" + \
           "bwkkkkkkkkkkkkkkkkkwb" + \
           "bwwwwwwwwwwwwwwwwwwwb" 

    def __init__(self, root):
        self.root = root
        self.currentMap = []
        self.currentMap[:] = self.startMap
        self.nKibbles = self.startMap.count
        self.gameFrame = Frame(self.root, bg = 'black')
        self.gameCanvas = Canvas(self.gameFrame, width = self.CELLSIZE * self.NROWSCOLUMNS, height = self.CELLSIZE * self.NROWSCOLUMNS, bg = 'black')
        self.gameCanvas.pack(side = TOP)
        self.blockType = {"b": PhotoImage(file = self.IMAGES + "Blank.gif"),
                 "k": PhotoImage(file = self.IMAGES + "Kibble.gif"),
                 "w": PhotoImage(file = self.IMAGES + "Wall.gif")}
        for i in range(self.TOTALCELLS):
            self.nRow = int(i % self.NROWSCOLUMNS)
            self.nColumn = int(i / self.NROWSCOLUMNS)
            #self.photo = PhotoImage(file = self.IMAGES + self.blockType[self.currentMap[i]])
            self.gameCanvas.create_image(self.nRow * 27 + (27 / 2) , self.nColumn * 27 + (27 / 2), image = self.blockType[self.currentMap[i]])


    def DrawMaze(self):
        for i in range(self.TOTALCELLS):
            self.photo = PhotoImage(file = self.IMAGES + self.blockType[self.currentMap[i]])
            self.cellCanvas[i].config(image = self.photo)
            