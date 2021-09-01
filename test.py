"""
Author          : 
Date Created    : 
Date Modified   : 
Version         : 
Description     : 
History         : 
"""

#Import required libraries
import pygame

def displayGrid(caption, grid):
    """
    Display grid in an easy to read format for the terminal
    """
    print("\n"+caption)
    for row in grid:
        print(row)

def createEmptyGrid():
    """
    10x10 matrix filled with zeros
    return: Returns a grid
    """
    grid=[]
    for row in range(10):
        grid.append([])
        for column in range(10):
            grid[row].append(0)
    
    displayGrid("Grid Creation",grid)
    return grid

def main():
    print("\n\
            --------------------------------------\n\
            ---- Welcome to the Game of Life! ----\n\
            --------------------------------------\n")

    # 10x10 matrix filled with zeros
    grid = createEmptyGrid()

    # Populate the initial grid spots
    grid[5][4]=1
    grid[4][4]=1
    grid[3][4]=1
    grid[4][3]=1
    grid[3][5]=1
    displayGrid("Initial grid spots", grid)

    sumGrid=[]
    for row in range(10):
        sumGrid.append([])
        for column in range(10):
            if column == 9 and row < 9:
                sum=(   (grid[row+1][column])+
                        (grid[row-1][column-1])+
                        (grid[row][column-1])+
                        (grid[row-1][column])+
                        (grid[row+1][column-1])) 
                sumGrid[row].append(sum)
            elif row == 9 and column < 9:
                sum=(   (grid[row][column+1])+
                        (grid[row-1][column-1])+
                        (grid[row][column-1])+
                        (grid[row-1][column])+
                        (grid[row-1][column+1])) 
                sumGrid[row].append(sum)
            elif row == 9 and column == 9:
                sum=(   (grid[row-1][column-1])+
                        (grid[row][column-1])+
                        (grid[row-1][column])) 
                sumGrid[row].append(sum)
            else:
                sum=(   (grid[row+1][column+1])+
                        (grid[row][column+1])+
                        (grid[row+1][column])+
                        (grid[row-1][column-1])+
                        (grid[row][column-1])+
                        (grid[row-1][column])+
                        (grid[row+1][column-1])+
                        (grid[row-1][column+1])) 
                sumGrid[row].append(sum)
    displayGrid("Grid with calculated sum", sumGrid)

if __name__ == "__main__":
    main()