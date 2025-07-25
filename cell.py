from tkinter import Button
import random
import settings

class Cell:
    all = []
    def __init__(self, x, y, is_mime = False):
        self.is_mine = is_mime
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

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()

    def right_click_actions(self, event):
        print("right button clicked!")

    def show_mine(self):
        '''
        logic to interrupt the game and display a message that player has lost as player clicked on a mine
        '''
        self.cell_btn_object.configure(bg='red')

    def show_cell(self):
        self.cell_btn_object.configure(text = self.surrounded_cells_mines_count)

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