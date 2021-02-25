
#details about each cell and used to find its neighbours and what is contained in a cell
class Cell():
    #constructor
    def __init__(self, row, col, nRowsColumns, cellType):
        self.row = row
        self.col = col
        self.nRowsColumns = nRowsColumns
        self.cellType = cellType
        open = False
        self.neighbours = []
    
    #get position
    def GetPos(self):
        return self.row, self.col
    
    #update what neighbours each cell has
    def UpdateNeighbours(self, grid):
        self.neighbours = []
        if self.cellType == "T":
            if self.col < self.nRowsColumns - 1 and grid[self.row][self.col + 1].cellType != "w": #Right
                self.neighbours.append(grid[self.row][self.col + 1])
            else:
                self.neighbours.append(grid[self.row][0])

            if self.col > 0 and grid[self.row][self.col - 1].cellType != "w": #Left
                self.neighbours.append(grid[self.row][self.col - 1])
            else:
                self.neighbours.append(grid[self.row][20])
        else:
            if self.col < self.nRowsColumns - 1 and grid[self.row][self.col + 1].cellType != "w": #Right
                self.neighbours.append(grid[self.row][self.col + 1])

            if self.col > 0 and grid[self.row][self.col - 1].cellType != "w": #Left
                self.neighbours.append(grid[self.row][self.col - 1])

        
        if self.row < self.nRowsColumns - 1 and grid[self.row + 1][self.col].cellType != "w": #Down
            self.neighbours.append(grid[self.row + 1][self.col])

        if self.row > 0 and grid[self.row - 1][self.col].cellType != "w": #Up
            self.neighbours.append(grid[self.row - 1][self.col])

