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
        self.cell_btn_object = btn