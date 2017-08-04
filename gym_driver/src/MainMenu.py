from MainPanel import MainPanel
from Map import Map
from Menu import Menu

class MainMenu(Menu):

    # MainMenu constructor
    def __init__(self, program):
        self.program = program
        Menu.__init__(self, program, "Main Menu", Map(0, 0))

    # Make a new MainPanel for the MainMenu
    def make_panel(self):
        return MainPanel(self.program, self)
