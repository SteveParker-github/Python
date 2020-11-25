import tkinter as tk
from tkinter import messagebox
import time

#constants
WINDOWHEIGHT = 700
WINDOWWIDTH = 1000
MAZESIZE = 588 
NROWSCOLUMNS = 21
CELLSIZE = 27
SPACESIZE = 1

#fields?
directionKeys = {0: 'w',
                 1: 'a',
                 2: 's',
                 3: 'd'}
startMap = "bwwwwwwwwwwwwwwwwwwwb" + \
           "bwkkkkkkkkwkkkkkkkkwb" + \
           "bwkwwkwwwkwkwwwkwwkwb" + \
           "bwkkkkkkkkkkkkkkkkkwb" + \
           "bwkwwkwkwwwwwkwkwwkwb" + \
           "bwkkkkwkkkwkkkwkkkkwb" + \
           "bwwwwkwwwbwbwwwkwwwwb" + \
           "bbbbwkwbbbbbbbwkwbbbb" + \
           "wwwwwkwbwwbwwbwkwwwww" + \
           "tbbbbkbbwbbbwbbkbbbbt" + \
           "wwwwwkwbwwwwwbwkwwwww" + \
           "bbbbwkwbbbbbbbwkwbbbb" + \
           "bwwwwkwbwwwwwbwkwwwwb" + \
           "bwkkkkkkkkwkkkkkkkkwb" + \
           "bwkwwkwwwkwkwwwkwwkwb" + \
           "bwkkwkkkkkbkkkkkwkkwb" + \
           "bwwkwkwkwwwwwkwkwkwwb" + \
           "bwkkkkwkkkwkkkwkkkkwb" + \
           "bwkwwwwwwkwkwwwwwwkwb" + \
           "bwkkkkkkkkkkkkkkkkkwb" + \
           "bwwwwwwwwwwwwwwwwwwwb"  
timer_enabled = False

#the main form
root = tk.Tk()
root.minsize(MAZESIZE, MAZESIZE+100)
root.maxsize(MAZESIZE, MAZESIZE+100)
root.title("Pacman")

def CreateMaze():
    xPos = CELLSIZE + SPACESIZE
    yPos = CELLSIZE + SPACESIZE
    for y in range(NROWSCOLUMNS):
        yPos = yPos * y
        for x in range(NROWSCOLUMNS):
            xPos = xPos * x



def DrawMaze():
    for x in startMap:
        print(x)

#the maze part
def maze():
    DrawMaze()

#playing with button
def button1_click():
   msg = messagebox.showinfo( "Hello World", "I did something!")
   print("you pressed something")

#pressed button event
def Key_Down(event):
    #finds if the key was to move or something else
    if event.char in directionKeys.values():
        print("you pressed the direction key ", repr(event.char))
    else:
        print("You didn't press the direction key, you pressed ", repr(event.char))

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

#allows the keyboard to be interactive
root.bind("<Key>", Key_Down)

#sets the width and height of the form
canvas = tk.Canvas(root, height = WINDOWHEIGHT, width = WINDOWWIDTH)
canvas.pack()

#declaring the frame
mainFrame = tk.Frame(root, bg = '#80c1ff')
mainFrame.place(relwidth=1, relheight=1)

#frame for the maze
mazeFrame = tk.Frame(mainFrame, bg = 'black')
mazeFrame.place(x = 0, y = 0, height = MAZESIZE, width = MAZESIZE)


#declaring the button
button1 = tk.Button(mainFrame, width = 10, text = "New Game", command = button1_click)
button1.place(relx = 0.1, y = MAZESIZE+50)

button2 = tk.Button(mainFrame, width = 10, text = "Start Game", command = button2_click)
button2.pack(side = tk.BOTTOM)
button2.place(relx = 0.45, y = MAZESIZE+50)

#start the form
root.mainloop()
