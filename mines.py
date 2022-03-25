import numpy as np
from random import sample
import pandas as pd

def border_check(grid,x_check,y_check):
    #Checks if the selected position is out of bounds
    if x_check <= -1 or x_check >= grid.shape[0]:
        return False
    if y_check <= -1 or y_check >= grid.shape[1]:
        return False
    return True

def gen_mines(grid_x,grid_y,count,mine='M'):
    #Generates a grid filled with mines, given an empty grid
    grid = np.zeros((grid_x,grid_y),dtype=object)

    #Finds all possible coords
    coords = []
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            coords.append((x,y))
    coords = sample(coords,count) #chooses random set of coords to place mines
    for coord in coords:
        grid[coord[0],coord[1]] = mine #places mines
        #loops through the surrounding cells
        for i in (-1,0,1):
            for j in (-1,0,1):
                if i==0 and j==0:
                    continue #skips if its the mine cell
                try:
                    if grid[coord[0]+i][coord[1]+j] != mine and border_check(grid,coord[0]+i, coord[1]+j):
                        grid[coord[0]+i][coord[1]+j] += 1
                except:
                    continue

    return grid

def display(grid):
    grid = pd.DataFrame(grid)
    return(grid.to_string(index = False, header = False))