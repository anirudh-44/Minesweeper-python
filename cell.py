from tkinter import Button, Label
import random
import settings
import ctypes # used to throw warnings (works in windows only)
import sys

class Cell:
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None

    def __init__(self, x, y, is_mine = False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_marked = False
        self.cell_btn_object = None
        self.x = x
        self.y = y

        # Append the object to the Cell.all list
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width = 12,
            height = 4,
        )
        btn.bind('<Button-1>', self.left_click_actions)  #<Button-1> this is the convention in tkinter for left click also, note that we are just passing the method reference and not calling it.
        btn.bind('<Button-3>', self.right_click_actions) #right click
        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label(location):
        label = Label(
            location,
            bg = 'black',
            fg = 'white',
            text = f"Cells left:{Cell.cell_count}",
            font=("Ariel", 30)
        )
        Cell.cell_count_label_object = label

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_count == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()

    def right_click_actions(self, event):
        if not self.is_marked:
            self.cell_btn_object.configure(
                bg='yellow'
            )
            self.is_marked = True
        else:
            self.cell_btn_object.configure(
                bg = 'SystemButtonFace'
            )
            self.is_marked = False

    def show_mine(self):
        '''
        logic to interrupt the game and display a message that player has lost as player clicked on a mine
        '''
        self.cell_btn_object.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0, 'You clicked on a mine', 'Game Over', 0)
        sys.exit()

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text = self.surrounded_cells_mines_count)
            # Replace the text of cell count label with the newer count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text = f"Cells left:{Cell.cell_count}"
                )
        # Mark the cell as opened (Use it as the last line of this method)
        self.is_opened = True

    def get_cell_by_axis(self, x, y):
        '''
        return cell object based on the value of x,y
        '''
        for cell in Cell.all:
            if (cell.x == x and cell.y == y):
                return cell

    @property   #read only attribute
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x -1, self.y -1),
            self.get_cell_by_axis(self.x -1, self.y),
            self.get_cell_by_axis(self.x -1, self.y +1),
            self.get_cell_by_axis(self.x, self.y -1),
            self.get_cell_by_axis(self.x, self.y +1),
            self.get_cell_by_axis(self.x +1, self.y -1),
            self.get_cell_by_axis(self.x +1, self.y),
            self.get_cell_by_axis(self.x +1, self.y +1),
        ]

        cells = [ cell for cell in cells if cell is not None ]
        return cells
    
    @property
    def surrounded_cells_mines_count(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter +=1
        
        return counter

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT 
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):                 
        '''
        we are overriding this method to display cell objects in a readable format instead
        of some memory addresses
        '''
        return f"Cell({self.x},{self.y})"