from Tkinter import\
    Button, Label, Entry,\
    X

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
PANEL_X = WINDOW_W - PANEL_W

# Panel class
class Panel:

    # Panel constructor
    def __init__(self, root, menu):
        self.root = root
        self.menu = menu
        self.add_buttons()

    # Getter method: map
    def get_map(self):
        return self.menu.get_map()

    # Setter method: map
    def set_map(self, map):
        self.menu.map.set_map(map)

    # Utility method for populating the Panel with a Label
    def add_label(self, text, x, y):
        label = Label(self.root, text=text)
        label.place(x=PANEL_X + x, y=y)

    # Utility method for populating the Panel with Buttons
    def add_button(self, text, y, cmd):
        button = Button(self.root, text=text, command=cmd)
        button.pack(fill=X)
        button.place(x=PANEL_X, y=y + MARGIN)

    # Utility method for populating the Panel with Label & Entry fields
    def add_text_field(self, label_text, field_text, y):
        self.add_label(label_text, y)
        text_field = Entry(self.root, text=field_text)
        text_field.place(x=PANEL_X + LABEL_W, y=y)

#     /** Utility method for populating the Panel with JButtons */
#     JButton addButton(String t, int x, int y, int w, int h,
#                               ActionListener a) {
#         JButton button = new JButton(t);
#         button.setBounds(x + MARGIN, y + MARGIN, w - MARGIN, h - MARGIN);
#         button.addActionListener(a);
#         button.setBorder(BorderFactory.createLineBorder(Color.BLACK));
#         add(button);
#         return button;
#     }
#
#     /** Populate the MakerPanel with back options */
#     void addBackOption() {
#         addButton("main menu", 0, BOTTOM, PANEL_W, INPUT_H,
#                 (ActionEvent a) -> changeScreen(new MainMenu()));
#     }
#
#     /** Get the Menu's Map */
#     Map getMap() {
#         return menu.map;
#     }
#
#     /** Get the Menu's JScrollPane */
#     JScrollPane getPane() {
#         return menu.scrollPane;
#     }
#
#     /** Set the Menu's Map to the one specified */
#     void setMap(Map m) {
#         menu.map = m;
#         menu.scrollPane.setViewportView(m);
#         updateFields();
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
