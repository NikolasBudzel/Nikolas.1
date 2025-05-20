# Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
from itertools import count

width = 20
height = 20

playground = []

def create_playground(width=20,height=20):
    temp = []
    for i in range(height):
        temp_in = []
        for i in range(width):
            temp_in.append(0)
        temp.append(temp_in)
    return (temp)

def create_cells(list_of_cells,playground):
    #list_of_cells = [(4,5),(5,8)]
    for cell in list_of_cells:
        playground[cell[1]][cell[0]]= 1

def get_neighbors(x,y):
    count = 0
    if x != 0:
        if(playground[y][x-1]==1):
            count += 1
    if x != width-1:
        if(playground[y][x+1]==1):
            count += 1
    if y != 0:
        if(playground[y-1][x]==1):
            count += 1
    if y != height-1:
        if(playground[y+1][x]==1):
            count += 1
    if y != 0 and x != 0:
        if(playground[y-1][x-1]==1):
            count += 1
    if y != 0 and x != width-1:
        if(playground[y-1][x+1]==1):
            count += 1
    if y != height-1 and x != 0:
        if(playground[y+1][x-1]==1):
            count += 1
    if y != height-1 and x != width-1:
        if(playground[y+1][x+1]==1):
            count += 1
    return count

def update_status(x,y):
    neighbors = get_neighbors(x,y)
    if playground[y][x] == 1 and neighbors < 2:
        return 0
    if playground[y][x] == 1 and (neighbors == 2 or neighbors ==3):
        return 1
    if playground[y][x] == 1 and neighbors > 3:
        return 0
    if playground[y][x] == 0 and neighbors == 3:
        return 1


playground=create_playground()
create_cells([(1,0),(2,1),(0,2),(1,2),(2,2)],playground)
for riadok in playground:
    print(riadok)
