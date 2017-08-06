from MainPanel import MainPanel
from Map import Map
from Menu import Menu

class MainMenu(Menu):

    # MainMenu constructor
    def __init__(self, root):
        Menu.__init__(self, root, "Main Menu", Map(0, 0))

    # Make a new MainPanel for the MainMenu
    def make_panel(self):
        return MainPanel(self.root, self)
