from tkinter import *
from subMain import SubMain

#HighScore page to tell the user the leaderboard in the game
class HighScore(SubMain):
    #constants
    MAXPLAYERS = 10
    #fields
    positions = ["1st",
                      "2nd",
                      "3rd",
                      "4th",
                      "5th",
                      "6th",
                      "7th",
                      "8th",
                      "9th",
                      "10th"]
    names = []
    scores = []
    positionLabels = []
    nameLabels = []
    scoreLabels = []
    colours = ["firebrick",
               "red",
               "orange",
               "goldenrod",
               "yellow",
               "lime",
               "green",
               "blue",
               "indigo",
               "violet"]
    #constructor
    def __init__(self, root):
        SubMain.__init__(self, root)
        self.titleLabel.configure(text = "HighScores!")

        self.scoreFrame = Frame(self.subMainFrame, bg = 'black')
        self.scoreFrame.pack(side = TOP)
        f = open("HighScores/HighScores.txt", "r")
        self.contents = f.read().splitlines()
        for i in range(10):
           self.names.append(self.contents[i * 2])
           self.scores.append(self.contents[i * 2 + 1])
           print(self.scores[i] + ", " + self.names[i])
        f.close()
        #create list of labels for positions, another list for player's name and another list for player's score
        for i in range(self.MAXPLAYERS):
            self.positionLabels.append(Label(self.scoreFrame, text = self.positions[i], font = "helvetica 20", fg = self.colours[i], bg = 'black'))
            self.positionLabels[i].grid(column = 0, pady = 10 , row = i)
            self.nameLabels.append(Label(self.scoreFrame, text = self.names[i], font = "helvetica 20", fg = self.colours[i], bg = 'black'))
            self.nameLabels[i].grid(column = 1, padx = 200, pady = 10, row = i)
            self.scoreLabels.append(Label(self.scoreFrame, text = self.scores[i], font = "helvetica 20", fg = self.colours[i], bg = 'black'))
            self.scoreLabels[i].grid(column = 2, pady = 10, row = i)




