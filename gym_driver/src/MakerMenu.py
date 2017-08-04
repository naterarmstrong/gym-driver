from Menu import Menu
from MakerPanel import MakerPanel

# MakerMenu class
class MakerMenu(Menu):

    # MakerMenu constructor
    def __init__(self, program, map):
        self.program = program
        Menu.__init__(self, program, "Map Maker", map)

    # Make a new MakerPanel for the MakerMenu
    def make_panel(self):
        return MakerPanel(self.program, self)
