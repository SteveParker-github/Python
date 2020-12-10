from tkinter import *
from maze import Maze
from pacman import Pacman
from ghost import Ghost
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
    gameStop = True
    nextLevel = False
    died = False
    lives = 3
    score = 0
    ghosts = []

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

        self.pacman = Pacman(self.maze.gameCanvas, "right", [10 * 27, 15 * 27], "pacman")
        self.ghosts.append(Ghost(self.maze.gameCanvas, "left", [10 * 27, 7 * 27], "blinky"))

        self.fruit = Fruit(self.maze.gameCanvas)

        self.mainGameFrame.bind_all("<Key>", self.Key_Down)

    def StartNewGame(self):
        self.mainGameFrame.pack(side = TOP, fill = BOTH, expand = True)
        self.gameTrackingFrame.pack(side = BOTTOM)
        self.maze.NewMap()
        self.pacman.CreateImage()
        self.ghosts[0].CreateImage()
        self.gameStop = False
        self.RunGame()

    def StartNextLevel(self):
        self.maze.NewMap()
        self.RestartGame()

    def RestartGame(self):
        self.pacman.ResetPosition()
        for i in range(len(self.ghosts)):
            self.ghosts[i].ResetPosition()
        self.nextLevel = False
        self.gameStop = False
        self.died = False
        self.RunGame()

    def GameOver(self):
        print("GameOver")

    def RunGame(self):
        self.pacman.Move(self.maze.currentMap)
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
        for i in range(len(self.ghosts)):
            self.ghosts[i].Move(self.maze.currentMap)


        for i in range(len(self.ghosts)):
            if self.ghosts[i].position == self.pacman.position:
                self.lives -= 1
                self.livesLabel.config(text = self.lives)
                self.gameStop = True
                self.died = True
        if self.maze.nKibbles == 0:
            self.gameStop = True
            self.nextLevel = True


        if not self.gameStop:
            self.root.after(200, self.RunGame)
        elif self.nextLevel:
            self.StartNextLevel()
        elif self.died:
            if self.lives == 0:
                self.GameOver()
            else:
                self.RestartGame()

    #pressed button event
    def Key_Down(self, event):
        #finds if the key was to move or something else
        if event.char in self.directionKeys:
            self.pacman.nextDirection = self.directionKeys[event.char]
        elif event.char == " ":
            self.gameStop = not self.gameStop
            if not self.gameStop:
                self.RunGame()
            else:
                print("show an image that the game has paused")
        else:
            print("You didn't press the direction key, you pressed ", repr(event.char))



