from tkinter import *
import os
from PIL import Image

class Maze():
    """description of class"""
    #constants
    NROWSCOLUMNS = 21
    CELLSIZE = 27
    TOTALCELLS = NROWSCOLUMNS * NROWSCOLUMNS
    IMAGES = os.getcwd() + "\\Resources\\Images\\"
    startMap = "bn--------N--------eb" + \
           "b|kkkkkkkk|kkkkkkkk|b" + \
           "b|k<>k<->kVk<->k<>k|b" + \
           "b|kkkkkkkkkkkkkkkkk|b" + \
           "b|k<>k^k<-N->k^k<>k|b" + \
           "b|kkkk|kkk|kkk|kkkk|b" + \
           "bw--ekW->bVb<-Ekn--sb" + \
           "bbbb|k|bbbbbbb|k|bbbb" + \
           "----skVbn-B-ebVkw----" + \
           "bbbb|kbb|bbb|bbk|bbbb" + \
           "----ek^bw---sb^kn----" + \
           "bbbb|k|bbbbbbb|k|bbbb" + \
           "bn--skVb<-N->bVkw--eb" + \
           "b|kkkkkkkk|kkkkkkkk|b" + \
           "b|k<ek<->kVk<->kn>k|b" + \
           "b|kk|kkkkkbkkkkk|kk|b" + \
           "bW>kVk^k<-N->k^kVk<Eb" + \
           "b|kkkk|kkk|kkk|kkkk|b" + \
           "b|k<--S->kVk<-S-->k|b" + \
           "b|kkkkkkkkkkkkkkkkk|b" + \
           "bw-----------------sb" 


    def __init__(self, mainGameFrame):
        self.mainGameFrame = mainGameFrame
        self.currentMap = []
        self.currentMap[:] = self.startMap
        self.nKibbles = self.startMap.count("k")
        self.gameFrame = Frame(self.mainGameFrame, bg = 'black')
        self.gameFrame.pack(side = TOP)
        self.gameCanvas = Canvas(self.gameFrame, width = self.CELLSIZE * self.NROWSCOLUMNS, height = self.CELLSIZE * self.NROWSCOLUMNS, bg = 'black')
        self.gameCanvas.pack(side = TOP)
        self.blockType = {"b": None,
                          "k": PhotoImage(file = self.IMAGES + "Kibble.gif"),
                          "n": PhotoImage(file = self.IMAGES + "CNWWall.gif"),
                          "e": PhotoImage(file = self.IMAGES + "CNEWall.gif"),
                          "w": PhotoImage(file = self.IMAGES + "CSWWall.gif"),
                          "s": PhotoImage(file = self.IMAGES + "CSEWall.gif"),
                          "-": PhotoImage(file = self.IMAGES + "SHWall.gif"),
                          "|": PhotoImage(file = self.IMAGES + "SVWall.gif"),
                          "N": PhotoImage(file = self.IMAGES + "TNWall.gif"),
                          "E": PhotoImage(file = self.IMAGES + "TEWall.gif"),
                          "W": PhotoImage(file = self.IMAGES + "TWWall.gif"),
                          "S": PhotoImage(file = self.IMAGES + "TSWall.gif"),
                          "^": PhotoImage(file = self.IMAGES + "EndNWall.gif"),
                          ">": PhotoImage(file = self.IMAGES + "EndEWall.gif"),
                          "<": PhotoImage(file = self.IMAGES + "EndWWall.gif"),
                          "V": PhotoImage(file = self.IMAGES + "EndSWall.gif"),
                          "B": PhotoImage(file = self.IMAGES + "Barrier.gif")}


        for i in range(self.TOTALCELLS):
            nRow = int(i % self.NROWSCOLUMNS)
            nColumn = int(i / self.NROWSCOLUMNS)
            self.gameCanvas.create_image(nRow * 27 + (27 / 2), 
                                         nColumn * 27 + (27 / 2), 
                                         image = self.blockType[self.currentMap[i]],
                                         tags = i)
                

    def RemoveKibble(self, cellNumber):
        self.currentMap[cellNumber] = "f"
        self.nKibbles -= 1
        self.gameCanvas.delete(cellNumber + 1)

    def UpdateFruit(self, location, char):
        self.currentMap[location] = char
        
