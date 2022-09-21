import random
import tkinter
master = tkinter.Tk()
master.title("MineSweeper")
buttons = []  
mines = []
row = 9
column = 9
def init(row,column):
    # mines count start at 1
    
    count = 1
    for irow in range (row):
        for icolumn in range (column):
            button = MyButton(master, str(count), 6, 2)
            count = count + 1
            buttons.append(button)
    for i in range (row):
        for j in range (column):
            # set up the button in the grid
            buttons[i*9+j].grid(row = i,column = j)
def set_mine():
    for i in range(9):
      mines.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
    random_list = []
    for i in range(10):
      x_position = random.randint(1,81)
      if x_position not in random_list:
        random_list.append(x_position)
    for each in random_list:
      x_position = each//9
      index = each - x_position * 9
      if index == 0:
        mines[x_position-1][8] = -999
      else:
        mines[x_position][index] = -999
    if mines[0][0] != -999:
      if mines[0][1] == -999:
            mines[0][0] += 1
      if mines[1][0] == -999:
            mines[0][0] += 1
      if mines[1][1] == -999:
            mines[0][0] += 1
    if mines[0][8] != -999:
      if mines[0][7] == -999:
            mines[0][8] += 1
      if mines[1][7] == -999:
            mines[0][8] += 1
      if mines[1][8] == -999:
            mines[0][8] += 1
    if mines[8][8] != -999:
      if mines[7][7] == -999:
        mines[8][8] += 1
      if mines[8][7] == -999:
         mines[8][8] += 1
      if mines[7][8] == -999:
        mines[8][8] += 1
    for i in range(1,8):
        if mines[0][i] != -999:
            if mines[0][i-1] == -999:
                mines[0][i] += 1
            if mines[0][i+1] == -999:
                mines[0][i] += 1
            if mines[1][i-1] == -999:
                mines[0][i] += 1
            if mines[1][i] == -999:
                mines[0][i] += 1
            if mines[1][i+1] == -999:
                mines[0][i] += 1    
    for i in range(1,8):
        if mines[8][i] != -999:
            if mines[8][i-1] == -999:
                mines[8][i] += 1
            if mines[8][i+1] == -999:
                mines[8][i] += 1
            if mines[7][i-1] == -999:
                mines[8][i] += 1
            if mines[7][i] == -999:
                mines[8][i] += 1
            if mines[7][i+1] == -999:
                mines[8][i] += 1
    for i in range(1,8):
        if mines[i][0] != -999:
            if mines[i-1][0] == -999:
                mines[i][0] += 1
            if mines[i+1][0] == -999:
                mines[i][0] += 1
            if mines[i-1][1] == -999:
                mines[i][0] += 1
            if mines[i][1] == -999:
                mines[i][0] += 1
            if mines[i+1][1] == -999:
                mines[i][0] += 1
    for i in range(1,8):
        if mines[i][8] != -999:
            if mines[i-1][8] == -999:
                mines[i][8] += 1
            if mines[i+1][8] == -999:
                mines[i][8] += 1
            if mines[i-1][7] == -999:
                mines[i][8] += 1
            if mines[i][7] == -999:
                mines[i][8] += 1
            if mines[i+1][7] == -999:
                mines[i][8] += 1
    for i in range(1,8):
        for j in range(1,8):
            if mines[i][j] != -999:
                if mines[i-1][j-1] == -999:
                    mines[i][j] += 1
                if mines[i+1][j+1] == -999:
                    mines[i][j] += 1
                if mines[i-1][j] == -999:
                    mines[i][j] += 1
                if mines[i-1][j+1] == -999:
                    mines[i][j] += 1
                if mines[i][j-1] == -999:
                    mines[i][j] += 1
                if mines[i][j+1] == -999:
                    mines[i][j] += 1
                if mines[i+1][j-1] == -999:
                    mines[i][j] += 1
                if mines[i+1][j] == -999:
                    mines[i][j] += 1     
class MyButton(tkinter.Button):
    # number of safety buttons left
    left = 71
    def __init__(self, obj, string, wid, hei):
        # flag = have a x_position in this cell
        self.flag = True
        # display the text on button
        self.strvar = tkinter.StringVar()
        # use super function to proxy object to delegate the class, command all atributes
        # cite from https://www.pythonforbeginners.com/super/working-python-super-function
        super(MyButton, self).__init__(obj, textvariable=self.strvar, width=wid, height=hei, command=self.checkMine)
        self.index = int(string)
    # set the text that will display on button        
    def settext(self, text):
        self.strvar.set(text)

    # check of  mines 
    def checkMine(self):
        # check of all safety buttons have been clicked or not
        if MyButton.left == 0:
            # game win
            win()
        # check of the clicekd button is a x_position or not
        else:
            index_x = 0
            if self.index < 10:
                index_y = self.index - 1
            else:
                x_position = self.index // 9
                index_y = self.index - x_position * 9
                if index_y == 0:
                    index_x = x_position - 1
                    index_y = 8
                else:
                    index_x = x_position
                    index_y = index_y - 1

            if mines[index_x][index_y] == -999:
                # gameover
                gameover()
            # display the mines surrounding this clicked button
            else:
                self.strvar.set(str(mines[index_x][index_y]))
                # safety button -= 1
                if self.flag:
                    MyButton.left -= 1

def win():
    if MyButton.left == 0:
        label_1 = tkinter.Label(master, text="Win", font=10).grid(row=1)
        print(label_1)

def gameover():
    # record of the position of mines and cound of mines
    record = []
    count = 0
    
    # find all the mines
    for item in mines:
        for i in item:
            if i == -999:
                record.append(count)
                count += 1
            else:
                count += 1
    # show all the mines
    for index in record:
        buttons[index]["fg"] = "red"
        buttons[index]["bg"] = "black"
        buttons[index].settext("×")

init(row,column)
set_mine()
master.mainloop()