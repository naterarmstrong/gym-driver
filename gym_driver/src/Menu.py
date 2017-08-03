from Tkinter import\
    PanedWindow, Scrollbar,\
    BOTH, LEFT, RIGHT, VERTICAL, HORIZONTAL, X, Y, BOTTOM

from read_config import read_config

configs = read_config()
WINDOW_WIDTH = configs["WINDOW_WIDTH"]
WINDOW_HEIGHT = configs["WINDOW_HEIGHT"]
PANE_WIDTH = configs["PANE_WIDTH"]
PANE_HEIGHT = configs["PANE_HEIGHT"]
BACKGROUND_COLOR = configs["BACKGROUND_COLOR"]

# Menu class
class Menu(PanedWindow):

    # Menu constructor
    def __init__(self, root, title, map,
                 width=WINDOW_WIDTH, height=WINDOW_HEIGHT):
        PanedWindow.__init__(self)
        self.root = root
        self.set_title(title)
        self.set_map(map)
        self.width = width
        self.height = height
        self.add_map_pane()

    # Getter method:
    def get_title(self):
        return self.title

    # Getter method: map
    def get_map(self):
        return self.map

    # Setter method: title
    def set_title(self, title):
        self.title = title

    # Setter method: map
    def set_map(self, map):
        self.map = map

    # Populate the Menu with a Map pane
    def add_map_pane(self):
        master = PanedWindow(bg=BACKGROUND_COLOR)
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
        master.config(width=PANE_WIDTH - 200, height=PANE_HEIGHT)
        master.add(canvas)
