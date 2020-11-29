from tkinter import *
from subMain import SubMain

#Instruction page to tell the user how to play the game
class Instruction(SubMain):
    #constants

    #fields
    instructionText = ["Guide Pacman around the maze and eat all the little white dots whilst avoiding those nasty ghosts.",
                       "If you eat a Power Pill, you can eat the ghosts!",
                       "Occasionally, a fruit appears which gives you a bonus score when eaten."]
    controlText = ["w,a,s,d to move pacman",
                   "more controls to come later"]
    #constructor
    def __init__(self, root):
        SubMain.__init__(self, root)
        self.titleLabel.configure(text = "Instructions!")

        self.goalLabel = Label(self.subMainFrame, text = "Goal", font = "helvetica 20", bg = 'black', fg = 'yellow')
        self.goalLabel.pack(side = TOP, pady = (50, 20))
        for i in range(len(self.instructionText)):
            Label(self.subMainFrame, text = self.instructionText[i], font = "helvetica 20", fg = 'white', bg = 'black').pack(side = TOP)
        self.controlLabel = Label(self.subMainFrame, text = "Controls", font = "helvetica 20", bg = 'black', fg = 'yellow')
        self.controlLabel.pack(side = TOP, pady = (50, 20))
        for i in range(len(self.controlText)):
            Label(self.subMainFrame, text = self.controlText[i], font = "helvetica 20", fg = 'white', bg = 'black').pack(side = TOP)


