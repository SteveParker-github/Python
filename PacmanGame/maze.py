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

    startMap = "bn--------N--------eb" + \
           "b|kkkkkkkk|kkkkkkkk|b" + \
           "b|k<>k<->kVk<->k<>k|b" + \
           "b|kkkkkkkkkkkkkkkkk|b" + \
           "b|k<>k^k<-N->k^k<>k|b" + \
           "b|kkkk|kkk|kkk|kkkk|b" + \
           "bw--ekW->bVb<-Ekn--sb" + \
           "bbbb|k|bbbbbbb|k|bbbb" + \
           "----skVbn-b-ebVkw----" + \
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
                 "V": PhotoImage(file = self.IMAGES + "EndSWall.gif")}
        for i in range(self.TOTALCELLS):
            self.nRow = int(i % self.NROWSCOLUMNS)
            self.nColumn = int(i / self.NROWSCOLUMNS)
            #self.photo = PhotoImage(file = self.IMAGES + self.blockType[self.currentMap[i]])
            self.gameCanvas.create_image(self.nRow * 27 + (27 / 2) , self.nColumn * 27 + (27 / 2), image = self.blockType[self.currentMap[i]])


    def DrawMaze(self):
        for i in range(self.TOTALCELLS):
            self.photo = PhotoImage(file = self.IMAGES + self.blockType[self.currentMap[i]])
            self.cellCanvas[i].config(image = self.photo)
            