from tkinter import Button

class Cell:
    def __init__(self, is_mime = False):
        self.is_mine = is_mime
        self.cell_btn_object = None

    def create_btn_object(self, location):
        btn = Button(
            location,
            text='Cell'
        )
        btn.bind('<Button-1>', self.left_click_actions)  #<Button-1> this is the convention in tkinter for left click also, note that we are just passing the method reference and not calling it.
        self.cell_btn_object = btn

    def left_click_actions(self, event):
        print("left button clicked!")