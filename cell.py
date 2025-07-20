from tkinter import Button
import random

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
            text = f'{self.x},{self.y}' 
        )
        btn.bind('<Button-1>', self.left_click_actions)  #<Button-1> this is the convention in tkinter for left click also, note that we are just passing the method reference and not calling it.
        btn.bind('<Button-3>', self.right_click_actions) #right click
        self.cell_btn_object = btn

    def left_click_actions(self, event):
        print("left button clicked!")

    def right_click_actions(self, event):
        print("right button clicked!")

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, 9
        )
        print(picked_cells)

    def __repr__(self):                 
        '''
        we are overriding this method to display cell objects in a readable format instead
        of some memory addresses
        '''
        return f"Cell({self.x},{self.y})"