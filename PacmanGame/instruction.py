from tkinter import *
from subMain import SubMain

#Instruction page to tell the user how to play the game
class Instruction(SubMain):
    #constants

    #fields

    #constructor
    def __init__(self, root):
        SubMain.__init__(self, root)
        self.titleLabel.configure(text = "Instructions!")

