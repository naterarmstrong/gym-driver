from os import listdir, path
from pickle import load
import tkFileDialog

from MakerMenu import MakerMenu
from Map import Map
from Panel import Panel

from read_config import read_config

configs = read_config()
SAVE_DIR = configs["SAVE_DIR"]
SAVE_EXT = configs["SAVE_EXT"]
WINDOW_W = configs["WINDOW_W"]
WINDOW_H = configs["WINDOW_H"]
PANEL_W = configs["PANEL_W"]
PANEL_H = configs["PANEL_H"]
MAP_LABEL_Y = configs["MAP_LABEL_Y"]
EDIT_MAP_Y = configs["EDIT_MAP_Y"]
RUN_MAP_Y = configs["RUN_MAP_Y"]
CYCLE_MAP_Y = configs["CYCLE_MAP_Y"]
NEW_MAP_Y = configs["NEW_MAP_Y"]
SELECT_MAP_Y = configs["SELECT_MAP_Y"]
MIDDLE = PANEL_W // 2

# MainPanel class
class MainPanel(Panel):

    # MainPanel constructor
    def __init__(self, program, main_menu):
        self.saves = MapList()
        if self.saves.get_size():
            self.set_map(self.saves.peek())
        Panel.__init__(self, program, main_menu)

    # Populate the MainPanel with buttons
    def add_buttons(self):
        self.add_map_name()
        self.add_edit_map()
        self.add_run_map()
        self.add_prev()
        self.add_next()
        self.add_select_map()
        self.add_new_map()

    def add_map_name(self):
        if self.saves.get_size():
            text = "Name: " + self.get_map().get_tag()
        else:
            text = "No Map Selected"
        self.add_label(text, MAP_LABEL_Y)

    def add_edit_map(self):
        self.add_button("Edit Map", 0, EDIT_MAP_Y, self.program.set_maker_menu)

    def add_run_map(self):
        def run_map():
            None
            # TODO: if saves.get_size(): change_screen(RunnerMenu(map))
        self.add_button("Run Map", 0, RUN_MAP_Y, run_map)

    def add_prev(self):
        def prev_map():
            if self.saves.get_size():
                prev = self.saves.prev()
                self.set_map(prev)
        self.add_button("<", 0, CYCLE_MAP_Y, prev_map, MIDDLE)

    def add_next(self):
        def next_map():
            if self.saves.get_size():
                next = self.saves.next()
                self.set_map(next)
        self.add_button(">", MIDDLE, CYCLE_MAP_Y, next_map, MIDDLE)

    def add_new_map(self):
        def new_map():
            self.change_screen(MakerMenu(self.program.root, Map()))
        self.add_button("New Map", 0, NEW_MAP_Y, new_map)

    def add_select_map(self):
        def select_map():
            try:
                filename = tkFileDialog.askopenfilename(initialdir="../maps/",
                                                        title="Select a Map")
                with open(filename, "r") as f:
                    map = load(f)
                self.set_map(map)
            except:
                print "Unsupported file type."
        self.add_button("Select Map", 0, SELECT_MAP_Y, select_map)

# TODO
#     /** Update fields in the MainPanel after changing the Map */
#     void updateFields() {
#         NAME_FIELD.setText(NAME_LABEL + getMap().getTag());
#     }

# MapList helper class
class MapList:

    # MapList constructor
    def __init__(self):
        self.saves = self.read_saves()
        self.index = 0

    # Read the saved maps
    @staticmethod
    def read_saves():
        saves = []
        for file in listdir(SAVE_DIR):
            if path.isfile(file) and path.splitext(file) == SAVE_EXT:
                with open(file, "rb") as f:
                    saved_map = load(f)
                    saves.append(saved_map)
        return saves

    # Getter method: size
    def get_size(self):
        return len(self.saves)

    # Get the current Map in the MapList
    def peek(self):
        return self.saves[self.index]

    # Get the previous Map in the MapList
    def prev(self):
        self.index = self.index - 1 if self.index else self.get_size() - 1
        return self.saves[self.index]

    # Get the next Map in the MapList
    def next(self):
        self.index = (self.index + 1) % self.get_size()
        return self.saves[self.index]