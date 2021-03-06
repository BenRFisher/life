"""
1. Initialize the cells in the grid.
2. At each time step in the simulation, for each 
cell (i, j) in the grid, do the following:
a. Update the value of cell (i, j) based on 
its neighbors, taking into account the 
boundary conditions.
b. Update the display of grid values.
"""

#attempt to make a grid

import pygame

#Constants for the grid design
BLACK = (0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
windowheight=255
windowwidth=255
size =(windowwidth,windowheight)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("my game")
done = False
clock = pygame.time.Clock()
width =20
height=20
margin=5


# 10x10 matrix filled with zeros
grid=[]
for row in range(11):
    grid.append([])
    for column in range(11):
        grid[row].append(0)

# Populate the initial grid spots
grid[6][5]=1
grid[5][5]=1
grid[4][5]=1
grid[5][4]=1
grid[4][6]=1
print(grid)
pygame.init()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    #game logic here

    #screen clear code here

    screen.fill(BLACK)
    for row in range(10):
        for column in range(10):
            colour=WHITE
            if grid[row][column]==1:
                colour = RED
            pygame.draw.rect(screen,colour,(((margin+width)*column +margin),((margin+height)*row +margin),width,height))
           

    clock.tick(60) #Frames per second, speed game runs
    pygame.display.flip()
    sum=[]
    #this bit is changing the grid array so that values which should be changed according to conways rules change from 1 to 0 or vice-versa
    #currently sum is accurately calculating the number of adjacent lit squares for each square, but isnt changing the grid array
    for row in range(10):
        for column in range(10):
            sum=((grid[row+1][column+1])+(grid[row][column+1])+(grid[row+1][column])+(grid[row-1][column-1])+(grid[row][column-1])+(grid[row-1][column])+(grid[row+1][column-1])+(grid[row-1][column+1]))            
            if grid[row][column]==1:
                if (sum<2) or (sum>3):
                    grid[row][column]=0
            else:
                if sum==3:
                    grid[row][column]=1
    done = True
        

print(grid)

    
pygame.quit()

        


