from tkinter import *
from maze import Maze
from pacman import Pacman

class Controller():
    """description of class"""
    #constants
    WINDOWHEIGHT = 700
    WINDOWWIDTH = 1000
    MAZESIZE = 588 

    #fields?
    directionKeys = {0: 'w',
                     1: 'a',
                     2: 's',
                     3: 'd'} 
    timer_enabled = False

    def __init__(self, root):
        self.root = root

        self.maze = Maze(self.root)

        self.gameTrackingFrame = Frame(self.root, bg = 'black')
        self.livesTitleLabel = Label(self.gameTrackingFrame, text = "Lives", bg = 'black', fg = 'white', font = "helvetica 20")
        self.livesTitleLabel.pack(side = LEFT)
        self.livesLabel = Label(self.gameTrackingFrame, text = "3", bg = 'black', fg = 'white', font = "helvetica 20")
        self.livesLabel.pack(side = LEFT)
        self.scoreTitleLabel = Label(self.gameTrackingFrame, text = "Score: ", bg = 'black', fg = 'white', font = "helvetica 20")
        self.scoreTitleLabel.pack(side = LEFT)
        self.scoreLabel = Label(self.gameTrackingFrame, text = "0", bg = 'black', fg = 'white', font = "helvetica 20")
        self.scoreLabel.pack(side = LEFT)

        self.pacman = Pacman(self.maze.gameCanvas)
    def StartNewGame(self):
        self.maze.gameFrame.pack(side = TOP, fill = BOTH, expand = True)
        self.gameTrackingFrame.pack(side = BOTTOM)
        self.RunGame()

    def RunGame(self):
        #self.pacman.MovePosition()
        self.pacman.MoveImage()
        self.root.after(200, self.RunGame)

    #when the timer runs do something
    def timer1_tick():
        print("tick")
        if timer_enabled:
            root.after(200, timer1_tick)

    #toggles the timer
    def button2_click():
        global timer_enabled 
        timer_enabled = not timer_enabled
        if timer_enabled:
            button2.configure(text = "Pause Game")
            timer1_tick()
        else:
            button2.configure(text = "Start Game")

