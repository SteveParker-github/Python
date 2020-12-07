from tkinter import *
from maze import Maze
from pacman import Pacman
from fruit import Fruit

class Controller():
    """description of class"""
    #constants
    WINDOWHEIGHT = 700
    WINDOWWIDTH = 1000
    MAZESIZE = 588 
    #fields?
    directionKeys = {"w": "up",
                     "a": "left",
                     "s": "down",
                     "d": "right"} 
    timer_enabled = False
    lives = 3
    score = 0

    def __init__(self, root):
        self.root = root

        self.mainGameFrame = Frame(self.root, bg = 'black')
        self.maze = Maze(self.mainGameFrame)
        self.gameTrackingFrame = Frame(self.mainGameFrame, bg = 'black')
        self.livesTitleLabel = Label(self.gameTrackingFrame, text = "Lives", bg = 'black', fg = 'white', font = "helvetica 20")
        self.livesTitleLabel.pack(side = LEFT)
        self.livesLabel = Label(self.gameTrackingFrame, text = self.lives, bg = 'black', fg = 'white', font = "helvetica 20")
        self.livesLabel.pack(side = LEFT)
        self.scoreTitleLabel = Label(self.gameTrackingFrame, text = "Score: ", bg = 'black', fg = 'white', font = "helvetica 20")
        self.scoreTitleLabel.pack(side = LEFT)
        self.scoreLabel = Label(self.gameTrackingFrame, text = self.score, bg = 'black', fg = 'white', font = "helvetica 20")
        self.scoreLabel.pack(side = LEFT)

        self.pacman = Pacman(self.maze.gameCanvas)

        self.fruit = Fruit(self.maze.gameCanvas)

        self.mainGameFrame.bind_all("<Key>", self.Key_Down)

    def StartNewGame(self):
        self.mainGameFrame.pack(side = TOP, fill = BOTH, expand = True)
        self.gameTrackingFrame.pack(side = BOTTOM)
        self.root.after(00, self.RunGame)


    def RunGame(self):
        #self.pacman.MovePosition()
        self.pacman.CheckNoWall(self.maze.currentMap)
        self.pacman.RedrawImage()
        if self.pacman.EatItem(self.maze.currentMap, "k"):
            self.maze.RemoveKibble(self.pacman.GetGridNumber())
            self.score += 10
            self.scoreLabel.config(text = self.score)

        if self.fruit.Run(self.maze.currentMap, self.maze.nKibbles):
            self.maze.UpdateFruit(self.fruit.fruitLocation, "F")
        if self.pacman.EatItem(self.maze.currentMap, "F"):
            self.fruit.RemoveFruit()
            self.maze.UpdateFruit(self.fruit.fruitLocation, "f")
            self.score += 100
            self.scoreLabel.config(text = self.score)
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

    #pressed button event
    def Key_Down(self, event):
        #finds if the key was to move or something else
        if event.char in self.directionKeys:
            self.pacman.nextDirection = self.directionKeys[event.char]
        else:
            print("You didn't press the direction key, you pressed ", repr(event.char))



