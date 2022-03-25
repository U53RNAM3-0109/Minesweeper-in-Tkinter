from tkinter import *
import tkinter.messagebox

#Example flag grid:
# True  False False False
# False False True  False
# True  False False True
# True  False False False

#Example player grid:
# 1 F 1 0 0
# 1 2 2 2 1
# 0 1 F 3 #
# 1 2 # # #
# 1 # # # #

#Example grid:
# 1 M 1 0 0
# 1 2 2 2 1
# 0 1 M 3 M
# 1 2 3 M 2
# 1 M 2 1 1

#Helper function
def is_flag(coord, flags):
    #Just returns the value in the thingy
    return flags[coord[0]][coord[1]]

def flag(coord, grid, flags, p_grid):
    #Very simple, if its a flag it becomes not a flag,
    #otherwise it becomes a flag
    if is_flag(coord, flags):
        flags[coord[0]][coord[1]] = False
    else:
        flags[coord[0]][coord[1]] = True
    return flags, p_grid

def clear(coord, grid, flags, p_grid):
    if not is_flag(coord, flags):
        return p_grid
    else:
        #Clear cell
        if grid[coord[0]][coord[1]] == 'M':
            #Mine!!
            end_game()
        else:
            p_grid[coord[0]][coord[1]] = grid[coord[0]][coord[1]]

            if grid[coord[0]][coord[1]] == 0:
                p_grid = clear_all(coord, grid, flags, p_grid)
                #This causes recursion. Its fine.

    return p_grid


def clear_all(coord, grid, flags, p_grid):
    #Calls clear function on all surrounding cells.
    for i in (-1,0,1):
            for j in (-1,0,1):
                if border_check(grid,coord[0]+i, coord[1]+j):
                    p_grid = clear((coord, grid, flags, p_grid))

    return p_grid


def 



def end_game():
    tkinter.messagebox.showinfo(
        'BOOOOM','''You set off a mine!!!
        you died
        '''
    )
