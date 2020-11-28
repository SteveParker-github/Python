class Maze():
    """description of class"""

    NROWSCOLUMNS = 21
    CELLSIZE = 27
    SPACESIZE = 1


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

    def __init__(self):
        something = something

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