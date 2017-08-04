from Tkinter import Button, Entry, PanedWindow, Label, BOTH, W

from read_config import read_config

configs = read_config()
SAVE_DIR = configs["SAVE_DIR"]
SAVE_EXT = configs["SAVE_EXT"]
WINDOW_W = configs["WINDOW_W"]
WINDOW_H = configs["WINDOW_H"]
PANE_W = configs["PANE_W"]
PANE_H = configs["PANE_H"]
PANEL_W = configs["PANEL_W"]
PANEL_H = configs["PANEL_H"]
LABEL_W = configs["LABEL_W"]
LABEL_H = configs["LABEL_H"]
MARGIN = configs["MARGIN"]
ELEMENT_H = configs["ELEMENT_H"]
PANEL_X = WINDOW_W - PANEL_W

# Panel class
class Panel:

    # Panel constructor
    def __init__(self, program, menu):
        self.program = program
        self.menu = menu
        self.add_buttons()

    # Getter method: map
    def get_map(self):
        return self.menu.get_map()

    # Setter method: map
    def set_map(self, map):
        self.menu.map.set_map(map)

    # Utility method for defining a window of specific dimensions
    def make_window(self, x, y, width, height):
        window = PanedWindow(self.program.frame)
        window.place(x=PANEL_X + x + MARGIN, y=y + MARGIN,
                     width=width - MARGIN, height=height - MARGIN)
        return window

    # Utility method for populating the Panel with a Label
    def add_label(self, text, y):
        window = self.make_window(0, y, PANEL_W, ELEMENT_H)
        label = Label(window, text=text)
        label.pack(anchor=W, expand=1)

    # Utility method for populating the Panel with Buttons
    def add_button(self, text, x, y, command, width=PANEL_W, height=ELEMENT_H):
        window = self.make_window(x, y, width, height)
        button = Button(window, text=text, command=command)
        button.pack(fill=BOTH, expand=1)

    # Utility method for populating the Panel with Label & Entry fields
    def add_text_field(self, label_text, field_text, y):
        self.add_label(label_text, y)
        window = self.make_window(LABEL_W, y, PANEL_W - LABEL_W, ELEMENT_H)
        text_field = Entry(window, text=field_text)
        text_field.pack(fill=BOTH, expand=1)

#     /** Populate the MakerPanel with back options */
#     void addBackOption() {
#         addButton("main menu", 0, BOTTOM, PANEL_W, INPUT_H,
#                 (ActionEvent a) -> changeScreen(new MainMenu()));
#     }
#
#     /** Change to a different screen */
#     void changeScreen(Menu newMenu) {
#         JFrame f = (JFrame) SwingUtilities.getWindowAncestor(menu);
#         f.remove(menu);
#         newScreen(f, newMenu);
#     }
#
#     /** Set up a new screen */
#     static void newScreen(JFrame f, Menu newMenu) {
#         f.setTitle(newMenu.getTitle());
#         f.getContentPane().add(newMenu);
#         f.pack();
#     }
#
#     /** Update fields in the Panel after changing the Map */
#     abstract void updateFields();
