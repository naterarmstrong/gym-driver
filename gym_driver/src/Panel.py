from read_config import read_config

configs = read_config()
SAVE_DIR = configs["SAVE_DIR"]
SAVE_EXT = configs["SAVE_EXT"]
WINDOW_WIDTH = configs["WINDOW_WIDTH"]
WINDOW_HEIGHT = configs["WINDOW_HEIGHT"]
PANE_WIDTH = configs["PANE_WIDTH"]
PANE_HEIGHT = configs["PANE_HEIGHT"]
PANEL_WIDTH = configs["PANEL_WIDTH"]
PANEL_HEIGHT = configs["PANEL_HEIGHT"]

# Panel class
class Panel:

    # Panel constructor
    def __init__(self, menu):
        self.menu = menu

#     /** Panel attributes */
#     static final int TOP           = 30;
#     static final int MIDDLE        = PANEL_WIDTH / 2;
#     static final int MARGIN        = 2;
#     static final int LABEL_W       = 50;
#     static final int INPUT_H       = 25;
#     static final int BOTTOM        = WINDOW_HEIGHT - INPUT_H - 60;
#     Menu menu;
#
#     /** Panel constructor */
#     Panel(MapMenu m) {
#         menu       = m;
#         setLayout(null);
#         setOpaque(false);
#         setVisible(true);
#         setPreferredSize(new Dimension(PANEL_WIDTH, PANEL_HEIGHT));
#     }
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
#         addButton("main menu", 0, BOTTOM, PANEL_WIDTH, INPUT_H,
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
