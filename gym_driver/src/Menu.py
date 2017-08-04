from Tkinter import\
    PanedWindow, Scrollbar,\
    BOTH, LEFT, RIGHT, VERTICAL, HORIZONTAL, X, Y, BOTTOM, Frame

from read_config import read_config

configs = read_config()
WINDOW_W = configs["WINDOW_W"]
WINDOW_H = configs["WINDOW_H"]
PANE_W = configs["PANE_W"]
PANE_H = configs["PANE_H"]
BACKGROUND_COLOR = configs["BACKGROUND_COLOR"]

# Menu class
class Menu(PanedWindow):

    # Menu constructor
    def __init__(self, program, title, map,
                 width=WINDOW_W, height=WINDOW_H):
        PanedWindow.__init__(self, program.frame)
        self.program = program
        self.set_title(title)
        self.set_map(map)
        self.width = width + 500
        self.height = height
        self.add_pane()
        self.add_panel()

    # Getter method:
    def get_title(self):
        return self.title

    # Getter method: map
    def get_map(self):
        return self.map

    # Setter method: title
    def set_title(self, title):
        self.title = title
        self.program.root.wm_title(self.get_title())

    # Setter method: map
    def set_map(self, map):
        self.map = map

    # Populate the Menu with a Map pane
    def add_pane(self):
        master = Frame(self.program.frame, bg=BACKGROUND_COLOR)
        master.pack(side=LEFT)
        master.propagate(0)
        canvas = self.get_map().get_canvas()
        hbar = Scrollbar(master, orient=HORIZONTAL)
        hbar.pack(side=BOTTOM, fill=X)
        hbar.config(command=canvas.xview)
        vbar = Scrollbar(master, orient=VERTICAL)
        vbar.pack(side=RIGHT, fill=Y)
        vbar.config(command=canvas.yview)
        canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        canvas.pack(side=LEFT, expand=True, fill=BOTH)
        master.config(width=PANE_W, height=PANE_H)

    # Populate the Menu with a Panel
    def add_panel(self):
        panel = self.make_panel()
