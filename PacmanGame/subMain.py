from tkinter import *

# the parent for instructions and highscores class
class SubMain:
    #constants

    #fields

    #constructor
    def __init__(self, root, goBackButton):
        self.root = root
        self.goBackButton = goBackButton

        self.subMainFrame = Frame(self.root, bg = 'black')
        self.titleLabel = Label(self.subMainFrame, text="title")
        
        self.titleLabel.pack(side = TOP)

    def Draw(self):
        self.subMainFrame.pack()
        self.goBackButton.pack(side = TOP)

    def Forget(self):
        self.subMainFrame.pack_forget()
        self.goBackButton.pack_forget()
