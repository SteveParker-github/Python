from tkinter import *

#Instruction page to tell the user how to play the game
class Instruction:
    #constants

    #fields

    #constructor
    def __init__(self, root, menuFrame, goBackButton):
        self.root = root
        self.menuFrame = menuFrame
        self.goBackButton = goBackButton
        self.instructionLabel = Label(self.root, text="Instructions!")

    def Draw(self):
        self.instructionLabel.pack(side = TOP)
        self.goBackButton.pack(side = TOP)

