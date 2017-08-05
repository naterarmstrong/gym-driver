from Tkinter import Tk, Frame, BOTH

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

# Program class
class Program:

    # Program constructor
    def __init__(self):
        self.root = Tk()
        self.root.resizable(width=False, height=False)
        self.root.config(width=WINDOW_W, height=WINDOW_H)
        self.root.propagate(0)
        self.frame = Frame(self.root)
        self.frame.pack(fill=BOTH, expand=1)
        self.set_main_menu()
        self.root.mainloop()

    # Clear the current frame
    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    # Set the frame to the MainMenu
    def set_main_menu(self):
        self.clear_frame()
        MainMenu(self)

    # Set the frame to the MakerMenu
    def set_maker_menu(self):
        self.clear_frame()
        MakerMenu(self, Map(self))

if __name__ == "__main__":
    main()
