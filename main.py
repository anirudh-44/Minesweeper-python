from tkinter import *
import settings
import utils

root = Tk()
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='red', # change later to black
    width = utils.width_prct(100),
    height = utils.height_prct(25)
)
top_frame.place(x=0,y=0)

left_frame = Frame(
    root,
    bg='blue', # change later to black
    width = utils.width_prct(25),
    height = utils.height_prct(75)
)
left_frame.place(x=0, y=utils.height_prct(25)) #left_frame.place(x=0,y=180)

# Run the window
root.mainloop() 