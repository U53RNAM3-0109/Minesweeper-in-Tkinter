import tkinter as tk
from math import floor
import grid_funcs
import mines
import numpy as np

global flags
global p_grid
global grid

x = 5
y = 5
mine_count = 5


flags = np.full((x,y), False)
p_grid = np.full((x,y), 'X')  # X = untouched, M = mine, 0-9 = 0-9
grid = mines.gen_mines(x,y,mine_count)


fakeCanv = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

def green_rect(event):
    x = floor((event.x) / 60)
    y = floor((event.y) / 60)
    x = min(x, 4)
    y = min(y, 4)
    colour = 1
    print(f"you clicked {x} X {y}")
    if colour_check(x, y, colour) == True:
      drawCanv.create_rectangle(x * 60,
                              y * 60, (x + 1) * 60, (y + 1) * 60,
                              outline="green",
                              fill="green")
    return (x, y)


def red_rect(event):
    x = floor((event.x) / 60)
    y = floor((event.y) / 60)
    x = min(x, 4)
    y = min(y, 4)
    colour = 2
    print(f"you clicked {x} X {y}")
    if colour_check(x,y,colour) == True:
      drawCanv.create_rectangle(x * 60,
                              y * 60, (x + 1) * 60, (y + 1) * 60,
                              outline="red",
                              fill="red")
    return (x, y)


def fix(event):
    print(f"you clicked {event.x} X {event.y}")
    x = floor((event.x) / 60)
    y = floor((event.y) / 60)
    print(f"you clicked {x} X {y}")
    x = min(x, 4)
    y = min(y, 4)
    print(f"you clicked {x} X {y}")
    drawCanv.delete(x, y, x + 60, y + 60)
    

def colour_check(x, y, colour):
  print(fakeCanv)
  if fakeCanv[x][y] == 0:
    fakeCanv[x][y] = colour
    return True
  else:
    return False
    

def reset(event):
    global fakeCanv
    fakeCanv = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    drawCanv.delete('all')

    for x in range(1, 540, 60):
        for y in range(1, 300, 60):
            rectangle = drawCanv.create_rectangle(x, y, x + 60, y + 60,\
                outline = 'black', fill = 'white')

def update_canvas(grid):
    grid_x = grid.shape[0]
    grid_y = grid.shape[1]

    #iterates through cells and draws them onto grid.
    #Might add an offset later so the grid isnt stuck in upper left.
    
    for x in range(0,grid_x):
        for y in range(0,grid_y):
            rectangle = drawCanv.create_rectangle(x*60, y*60, x*60 + 60, y*60 + 60,\
                outline = 'black', fill = cell_locate(x,y,grid))
            
            
            if grid[x][y] in (1,2,3,4,5,6,7,8):
                drawCanv.create_text(x*60+30,y*60+30,fill="Black",
                            text=str(grid[x][y]))


root = tk.Tk()
drawCanv = tk.Canvas(width=300, height=300, bd=0)
drawCanv.bind('<Button-1>', green_rect) # left click
drawCanv.bind('<Button-2>', reset) # middle click
drawCanv.bind('<Button-3>', red_rect) # right click

drawCanv.pack()

root.mainloop()



'''
def click_func(event):
    x = floor((event.x) / 60)
    y = floor((event.y) / 60)
    x = min(x, 4)
    y = min(y, 4)

    flags, p_grid = grid_func.func((x,y),grid,flags,p_grid)
    update(p_grid)

def right_click(event):
    x = floor((event.x) / 60)
    y = floor((event.y) / 60)
    x = min(x, 4)
    y = min(y, 4)

    flags, p_grid = grid_funcs.flag((x,y),grid,flags,p_grid)
    update_canvas(p_grid)

def left_click(event):
    x = floor((event.x) / 60)
    y = floor((event.y) / 60)
    x = min(x, 4)
    y = min(y, 4)

    p_grid = grid_funcs.clear((x,y),grid,flags,p_grid)
    update_canvas(p_grid)

def middle_click(event): #dont bind yet
    x = floor((event.x) / 60)
    y = floor((event.y) / 60)
    x = min(x, 4)
    y = min(y, 4)

    p_grid = grid_funcs.safe_clear((x,y),grid,flags,p_grid)
    update_canvas(p_grid)
'''