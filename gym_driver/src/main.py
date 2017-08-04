from Tkinter import Tk, Frame, BOTH
from tkinter import ttk

from MainMenu import MainMenu
from MakerMenu import MakerMenu
from Map import Map

from read_config import read_config

configs = read_config()
WINDOW_W = configs["WINDOW_W"]
WINDOW_H = configs["WINDOW_H"]

# Run the FORDS app
def main():
    Program()

class Program:

   def __init__(self):
       self.root = Tk()
       self.root.config(width=WINDOW_W, height=WINDOW_H)
       self.root.propagate(0)
       self.frame = Frame(self.root)
       self.frame.pack(fill=BOTH, expand=1)
       self.frame.config(bg="yellow")
       self.make_main_menu()
       self.root.mainloop()

   def clear_frame(self):
       for widget in self.program.frame.winfo_children():
           widget.destroy()

   def make_main_menu(self):
       self.clear_frame()
       MainMenu(self)

   def make_maker_manu(self):
       self.clear_frame()
       MakerMenu(self, Map(0,0))


if __name__ == "__main__":
    main()


# TODO: make the windows re-sizable, and have the map adjust to take up the extra space
