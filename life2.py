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

def gridinitialise():
    # 10x10 matrix filled with zeros
    grid=[]
    for row in range(21):
        grid.append([])
        for column in range(21):
            grid[row].append(0)
    """
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            column=pos[0]//(width+margin)
            row =pos[1]//(height+margin)
            grid[row][column]=1
    # Populate the initial grid spots
    
    grid[5][4]=1
    grid[4][4]=1
    grid[3][4]=1
    grid[4][3]=1
    grid[3][5]=1
    """
    pygame.init()
    return grid

def gridCalculate(grid):
    sumarray=[]
    for row in range(20):
        sumarray.append([])
        for column in range(20):
            sum=((grid[row+1][column+1])+(grid[row][column+1])+(grid[row+1][column])+(grid[row-1][column-1])+(grid[row][column-1])+(grid[row-1][column])+(grid[row+1][column-1])+(grid[row-1][column+1])) 
            sumarray[row].append(sum)
                
    #print(sumarray)
        #this bit is changing the grid array so that values which should be changed according to conways rules change from 1 to 0 or vice-versa
        #currently sum is accurately calculating the number of adjacent lit squares for each square, but isnt changing the grid array
    for row in range(20):
        for column in range(20):
            if grid[row][column]==1:
                if sumarray[row][column]<=1:
                    grid[row][column]=0
                elif sumarray[row][column]>=4:
                    grid[row][column]=0
            else:
                if sumarray[row][column]==3:
                    grid[row][column]=1
    return grid
    

    #game logic here
    #   #screen clear code here

def graphicprint(WHITE,BLACK,RED,margin,width,height,screen,clock,grid):
    screen.fill(BLACK)
    for row in range(20):
        for column in range(20):
            colour=WHITE
            if grid[row][column]==1:
                colour = RED
            pygame.draw.rect(screen,colour,(((margin+width)*column +margin),((margin+height)*row +margin),width,height))
    clock.tick(10)#tick speed
    pygame.display.flip()

def clickgraphicprint(WHITE,BLACK,RED,margin,width,height,screen,grid):
    done=False
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:# If user clicked close
                    done = True  # Flag that we are done so we exit this loop
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (width + margin)
                row = pos[1] // (height + margin)
                # Set that location to one
                grid[row][column] = 1
    
        screen.fill(BLACK)
        for row in range(20):
            for column in range(20):
                colour=WHITE
                if grid[row][column]==1:
                    colour = RED
                pygame.draw.rect(screen,colour,(((margin+width)*column +margin),((margin+height)*row +margin),width,height))
        
        pygame.display.flip()
    return grid
           
def main():
    #print("checkpoint 1")
    import pygame
    BLACK = (0,0,0)
    WHITE=(255,255,255)
    RED=(255,0,0)
    windowheight=500
    windowwidth=500
    size =(windowwidth,windowheight)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("my game")
    done = False
    clock = pygame.time.Clock()
    width =20
    height=20
    margin=5

    grid = gridinitialise()
    grid=clickgraphicprint(WHITE,BLACK,RED,margin,width,height,screen,grid)
    """
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RETURN:
                """
    while not done:
        graphicprint(WHITE,BLACK,RED,margin,width,height,screen,clock,grid)
        gridCalculate(grid)
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
        #print(grid)
     


    
if __name__ == "__main__":
    main()