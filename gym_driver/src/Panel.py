from Tkinter import Label, Entry

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

# Panel class
class Panel:

    # Panel constructor
    def __init__(self, menu):
        self.menu = menu
        self.add_buttons()

    # Utility method for populating the Panel with Text field
    def add_text_field(self, label_text, field_text, y):
        label = Label(self.menu.root, text=label_text)
        label.place(x=0, y=y)
        text_field = Entry(self.menu.root, text=field_text)
        text_field.place(x=30, y=y)

#     /** Panel attributes */
#     static final int MIDDLE        = PANEL_W / 2;
#     static final int MARGIN        = 2;
#     static final int LABEL_W       = 50;
#     static final int INPUT_H       = 25;
#     static final int BOTTOM        = WINDOW_H - INPUT_H - 60;
#     Menu menu;
#
#     /** Utility method for populating the Panel with TextFields */
#     TextField addTextField(String lTx, String fTx, int y, int w) {
#         Label label = new Label(lTx);
#         label.setBackground(Color.WHITE);
#         label.setBounds(0, y, LABEL_W, INPUT_H);
#         TextField field = new TextField(fTx);
#         field.setBounds(LABEL_W, y, w, INPUT_H);
#         add(label);
#         add(field);
#         return field;
#     }
#
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
