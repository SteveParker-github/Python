import math
import os
from queue import PriorityQueue
from cell import Cell

#constants
NROWSCOLUMNS = 21
startMap = ["bn--------N--------eb",
            "b|kkkkkkkk|kkkkkkkk|b",
            "b|k<>k<->kVk<->k<>k|b",
            "b|kkkkkkkkkkkkkkkkk|b",
            "b|k<>k^k<-N->k^k<>k|b",
            "b|kkkk|kkk|kkk|kkkk|b",
            "bw--ekW->bVb<-Ekn--sb",
            "bbbb|k|bbbbbbb|k|bbbb",
            "----skVbn-B-ebVkw----",
            "Tbbbbkbb|bbb|bbkbbbbT",
            "----ek^bw---sb^kn----",
            "bbbb|k|bbbbbbb|k|bbbb",
            "bn--skVb<-N->bVkw--eb",
            "b|kkkkkkkk|kkkkkkkk|b",
            "b|k<ek<->kVk<->kn>k|b",
            "b|kk|kkkkkbkkkkk|kk|b",
            "bW>kVk^k<-N->k^kVk<Eb",
            "b|kkkk|kkk|kkk|kkkk|b",
            "b|k<--S->kVk<-S-->k|b",
            "b|kkkkkkkkkkkkkkkkk|b",
            "bw-----------------sb"] 

pacmanLocationx = 2
pacmanlocationy = 5
ghostlocationx = 17
ghostlocationy = 9

WALLS = ["n", "e", "w", "s", "N", "E", "W", "S", "^", "<", "V", ">", "|", "-"]
SPACE = ["b", "k", "B"]

#make the grid 
def MakeGrid():
    grid = []

    for i in range(NROWSCOLUMNS):
        grid.append([])
        for j in range(NROWSCOLUMNS):
            cell = Cell(i, j, NROWSCOLUMNS, currentMap[i][j])
            grid[i].append(cell)

    return grid

#print cell map onto the console
def PrintCellMap(grid):
    for i in range(NROWSCOLUMNS):
        temp = ""
        for j in range(NROWSCOLUMNS):
            temp += grid[i][j].cellType
        print(temp)

#to find the f score
def h(p1, p2):
	x1, y1 = p1
	x2, y2 = p2
	return abs(x1 - x2) + abs(y1 - y2)

#backtrack to create path
def reconstruct_path(came_from, current):
    while current in came_from:
        current = came_from[current]
        if current.cellType != "S":
            current.cellType = "*"

#the main calculation to find the shortest path
def algorithm(grid, start, end):
	count = 0
	open_set = PriorityQueue()
	open_set.put((0, count, start))
	came_from = {}
	g_score = {cell: float("inf") for row in grid for cell in row}
	g_score[start] = 0
	f_score = {cell: float("inf") for row in grid for cell in row}
	f_score[start] = h(start.GetPos(), end.GetPos())

	open_set_hash = {start}

	while not open_set.empty():

		current = open_set.get()[2]
		open_set_hash.remove(current)

		if current == end:
			reconstruct_path(came_from, end)
			return True

		for neighbour in current.neighbours:
			temp_g_score = g_score[current] + 1

			if temp_g_score < g_score[neighbour]:
				came_from[neighbour] = current
				g_score[neighbour] = temp_g_score
				f_score[neighbour] = temp_g_score + h(neighbour.GetPos(), end.GetPos())
				if neighbour not in open_set_hash:
					count += 1
					open_set.put((f_score[neighbour], count, neighbour))
					open_set_hash.add(neighbour)
					neighbour.open = True

		if current != start:
			current.open = False

	return False


#main method
def main():
    global currentMap
    currentMap = startMap
    for i in range(len(currentMap)):
        for j in range(len(WALLS)):
            currentMap[i] = currentMap[i].replace(WALLS[j], "w")
        for j in range(len(SPACE)):
            currentMap[i] = currentMap[i].replace(SPACE[j], " ")

    grid = MakeGrid()
    for row in grid:
        for cell in row:
            cell.UpdateNeighbours(grid)
    
    start = None
    end = None

    cell = grid[ghostlocationy][ghostlocationx]
    start = cell
    start.cellType = "S"
    cell = grid[pacmanlocationy][pacmanLocationx]
    end = cell
    end.cellType = "E"
    PrintCellMap(grid)
    input("press any key to find the location")
    cls = lambda: print('\n'*100)
    cls()
    algorithm(grid, start, end)
    PrintCellMap(grid)

    


main()