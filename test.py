import random
import tkinter
master = tkinter.Tk()
master.title("MineSweeper")
buttons = []  
mines = []
row = 9
column = 9
def init(row,column):
  count = 1
  for irow in range(row):
    for icolumn in range(column):
      button = MyButton(master, str(count), 6, 2)
      count = count + 1
      buttons.append(button)
  for irow in range(row):
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