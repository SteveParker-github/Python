from tkinter import *

# the parent for instructions and highscores class
class SubMain:
    #constants

    #fields

    #constructor
    def __init__(self, root):
        self.root = root

        self.subMainFrame = Frame(self.root, bg = 'black')
        self.titleLabel = Label(self.subMainFrame, text="title", font = "helvetica 30", bg = 'black', fg = 'white')
        
        self.titleLabel.pack(side = TOP)

    def Draw(self):
        self.subMainFrame.pack(fill = BOTH, expand = True)

    def Forget(self):
        self.subMainFrame.pack_forget()
