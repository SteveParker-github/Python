from tkinter import *
from subMain import SubMain

#HighScore page to tell the user the leaderboard in the game
class HighScore(SubMain):
    #constants

    #fields

    #constructor
    def __init__(self, root, goBackButton):
        SubMain.__init__(self, root, goBackButton)
        self.titleLabel.configure(text = "HighScores!")


