#this game in only texted based unfortunately
#perhaps later we can transfer the code so that it works with a GUI


import random

def Mine_Sweeper_Map(size, mineCount):
    #creates a 2d array that acts as a grid
    arr = [[0 for row in range(size)] for column in range(size)] #creates grid with n sides
    #randomly generates mines k times
    for num in range(mineCount):
        x = random.randint(0,size-1)
        y = random.randint(0,size-1)
        arr[y][x] = 'X'

        #counts boxes adjacent and puts value to them if mine nearby
        #code is super long, maybe could find a way to make shorter
        if (x >=0 and x <= size-2) and (y >= 0 and y <= size-1):
            if arr[y][x+1] != 'X':
                arr[y][x+1] += 1 
        if (x >=1 and x <= size-1) and (y >= 0 and y <= size-1):
            if arr[y][x-1] != 'X':
                arr[y][x-1] += 1
        if (x >= 1 and x <= size-1) and (y >= 1 and y <= size-1):
            if arr[y-1][x-1] != 'X':
                arr[y-1][x-1] += 1 
 
        if (x >= 0 and x <= size-2) and (y >= 1 and y <= size-1):
            if arr[y-1][x+1] != 'X':
                arr[y-1][x+1] += 1
        if (x >= 0 and x <= size-1) and (y >= 1 and y <= size-1):
            if arr[y-1][x] != 'X':
                arr[y-1][x] += 1
 
        if (x >=0 and x <= size-2) and (y >= 0 and y <= size-2):
            if arr[y+1][x+1] != 'X':
                arr[y+1][x+1] += 1
        if (x >= 1 and x <= size-1) and (y >= 0 and y <= size-2):
            if arr[y+1][x-1] != 'X':
                arr[y+1][x-1] += 1
        if (x >= 0 and x <= size-1) and (y >= 0 and y <= size-2):
            if arr[y+1][x] != 'X':
                arr[y+1][x] += 1
    return arr

#creates the visible interactable map (purely textbase)
def Player_Map(size):
    arr = [['#' for row in range(size)] for column in range(size)]
    return arr

def create_Map():
    sc = turtle.Screen()
    grid = turtle.Turtle()
    sc.setworldcoordinates(0,0,90,90)
    grid.speed(0)
    grid.down()
    grid.goto(0,90)
    grid.goto(90,90)
    grid.goto(90,0)
    grid.goto(0,0)

    for x in range(1,10):
        grid.forward(5)
        grid.write(str(x))
        grid.forward(5)
        grid.setheading(90)
        grid.down()
        grid.forward(90)
        grid.up()
        grid.setheading(270)
        grid.forward(90)
        grid.setheading(0)

    grid.up()
    grid.goto(-1,0)
    grid.setheading(90)
    for y in range(1,10):
        grid.forward(5)
        grid.write(str(y))
        grid.forward(5)
        grid.setheading(0)
        grid.down()
        grid.forward(90)
        grid.up()
        grid.setheading(180)
        grid.forward(90)
        grid.setheading(90)
        

def markMap(xcord,ycord,turtle):
    turtle.goto(xcord,ycord)
    
    

def MineSweeper():
    #these two check whether or not the game is over and when it is lost 
    #can be used later in order to create an end game screen
    NotOver = True
    GameLost = False
    
    #can select the size/mineCount of the map here
    size = 9
    mineCount = 10
    
    mineSweeperMap = Mine_Sweeper_Map(size, mineCount)
    playerMap = Player_Map(size)

    #counts the moves of the player to know when the game is supposed
    #to end, ends when max moves is reach/when they hit a mine
    moveCount = (size**2 - mineCount)
    while (NotOver == True) or (moveCount > 0):
        print("Enter your cell you want to open :")
        xcord = input("input the x co-ord: ")
        ycord = input("input the y co-ord: ")
        xcord = int(xcord) - 1 
        ycord = int(ycord) - 1
        if (mineSweeperMap[ycord][xcord] == 'X'):
            print("Game Over!")
            for row in mineSweeperMap:
                print(" ".join(str(cell) for cell in row))
                print("")
                NotOver = False
                GameLost = True
        else:
            #reveals the x/y 
            playerMap[ycord][xcord] = mineSweeperMap[ycord][xcord]
            for row in playerMap:
                print(" ".join(str(cell) for cell in row))
                print("")
            moveCount = moveCount - 1

#last steps is to create an end screen and maybe a play again screen
        
        
#the only executable
MineSweeper()
                 

