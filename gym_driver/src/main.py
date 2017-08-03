from Tkinter import Tk, Frame

from MainMenu import MainMenu

from read_config import read_config

configs = read_config()
WINDOW_WIDTH = configs["WINDOW_WIDTH"]
WINDOW_HEIGHT = configs["WINDOW_HEIGHT"]

# Run the FORDS app
def main():
    root = Tk()
    root.config(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    root.propagate(0)
    frame = Frame(root)
    main_menu = MainMenu(root)
    root.mainloop()

if __name__ == "__main__":
    main()

# TODO: make the windows re-sizable, and have the map adjust to take up the extra space
