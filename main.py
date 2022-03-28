import mines
import tkinter as tk
import numpy as np
import time

def cell_locate(x,y,grid):
    colours = {
        'X':'Gray', #untouched
        0:'Silver',
        1:'Silver',
        2:'Silver',
        3:'Silver',
        4:'Silver',
        5:'Silver',
        6:'Silver',
        7:'Silver',
        8:'Silver',
        'M':'Black' #mine
    }
    return colours[grid[x][y]]

grid_x = 5
grid_y = 5

grid = np.full((grid_x,grid_y), 'X')#mines.gen_mines(5,5,5)
print(mines.display(grid))

#GENERATE CANVAS
root = tk.Tk()
drawCanv = tk.Canvas(width=grid_x*60+60, height=grid_y*60+60, bd=0)
drawCanv.pack()

def update_canvas(grid):
    grid_x = grid.shape[0]
    grid_y = grid.shape[1]
    
    for x in range(0,grid_x):
        for y in range(0,grid_y):
            rectangle = drawCanv.create_rectangle(x*60, y*60, x*60 + 60, y*60 + 60,\
                outline = 'black', fill = cell_locate(x,y,grid))
            
            
            if grid[x][y] in (1,2,3,4,5,6,7,8):
                drawCanv.create_text(x*60+30,y*60+30,fill="Black",
                            text=str(grid[x][y]))

root.mainloop()