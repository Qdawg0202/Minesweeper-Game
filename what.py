#Shell code for grid class:
import turtle
import random
import math

#b for beginner
#i for intermediate
#h for hard

class MineGrid():
    def __init__(self,level):
        gridRow = []
        gridColumn = []
        if level == 'b':
            for x in range(9):
                gridColumn.append('-')
            for y in range (9):
                gridRow.append(gridColumn)
                
mn = MineGrid(b)
            
          
          
          