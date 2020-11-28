from tkinter import *
import random
import winsound
import os
from instruction import Instruction 
from highScore import HighScore

class Main:
    #constants
    WINDOWWIDTH = 800
    WINDOWHEIGHT = 600
    RESOURCES = os.getcwd() + "\\Resources\\"
    AUDIO = "Audio\\"
    IMAGES = "Images\\"
    #Fields
    colours = ["red",
               "orange",
               "yellow",
               "green",
               "blue",
               "indigo",
               "violet"]
    word = ["P","A","C","M","A","N"]
    labels = []
    counter = 0

    def __init__(self):
        self.root = Tk()
        self.root.title = "Pacman"
        self.root.minsize(self.WINDOWWIDTH, self.WINDOWHEIGHT)

        #self.canvas = Canvas(self.root, width = self.WINDOWWIDTH, height = self.WINDOWHEIGHT)
        #self.canvas.pack()
        self.menuFrame = Frame(self.root, bg = 'black')
        self.titleFrame = Frame(self.menuFrame, bg = 'black')

        for x in range(6):
            self.labels.append(Label(self.titleFrame, text = self.word[x], font = "helvetica 70", fg = self.colours[x], bg = 'black'))
            self.labels[x].grid(column = x * 1, row = 0)

        self.playGameButton = Button(self.menuFrame, width = 10, text = "Play Game", command = self.PlayGame)
        self.highScoreButton = Button(self.menuFrame, width = 10, text = "HighScore", command = self.HighScores)
        self.instructionButton = Button(self.menuFrame, width = 10, text = "Instructions", command = self.Instructions)
        self.exitButton = Button(self.menuFrame, width = 10, text = "Exit", command = self.Exit)
        self.goBackButton = Button(self.root, text = "go back", command = self.GoBack)

        self.titleFrame.pack(side = TOP, pady = (20, 20))
        self.playGameButton.pack(side = TOP, pady = (20, 20))
        self.highScoreButton.pack(side = TOP, pady = (20, 20))
        self.instructionButton.pack(side = TOP, pady = (20, 20))
        self.exitButton.pack(side = TOP, pady = (20 , 0))

        self.instructionMenu = Instruction(self.root, self.goBackButton)
        self.highScoreMenu = HighScore(self.root, self.goBackButton)

    #the main form
    def MainMenu(self):
        self.menuFrame.place(relwidth = 1, relheight = 1)
        self.ChangeColour()
        self.Play()
        self.root.mainloop()
    
    def Play(self):
        location = self.RESOURCES + self.AUDIO + "PacmanMain.wav"
        winsound.PlaySound(location, winsound.SND_ASYNC)

    def ChangeColour(self):
        self.counter += 1

        for x in range(6):
            self.labels[x].config(fg = self.colours[(x + self.counter) % 7])

        self.root.after(400, self.ChangeColour)

    def PlayGame(self):
        self.menuFrame.place_forget()
        #self.game = Game(root)
        #self.game.Run()
        winsound.PlaySound(self.RESOURCES + self.AUDIO + 'StartGame.wav', winsound.SND_ASYNC)

    def HighScores(self):
        winsound.PlaySound(None, winsound.SND_PURGE)
        self.menuFrame.place_forget()
        self.highScoreMenu.Draw()

    def Instructions(self):
        winsound.PlaySound(None, winsound.SND_PURGE)
        self.menuFrame.place_forget()
        self.instructionMenu.Draw()

    def Exit(self):
        winsound.PlaySound(None, winsound.SND_PURGE)
        raise SystemExit()

    def GoBack(self):
        self.instructionMenu.Forget()
        self.highScoreMenu.Forget()
        self.menuFrame.place(relwidth = 1, relheight = 1)

    #start the form
if __name__ == '__main__':
    form1 = Main()
    form1.MainMenu()