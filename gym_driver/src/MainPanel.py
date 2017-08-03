from Tkinter import Label
from os import listdir, path
from pickle import load

from Panel import Panel

from read_config import read_config

configs = read_config()
SAVE_DIR = configs["SAVE_DIR"]
SAVE_EXT = configs["SAVE_EXT"]
PANEL_W = configs["PANEL_W"]
PANEL_H = configs["PANEL_H"]

# MainPanel class
class MainPanel(Panel):

    # MainPanel constructor
    def __init__(self, main_menu):
        self.saves = MapList()
        if self.saves.get_size():
            self.set_map(self.saves.peek())
        Panel.__init__(self, main_menu)

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
        self.name_field = Label(text=text)


    # /** Populate the MainPanel with a label corresponding to its Map's name */
    #     private void addNameLabel() {
    #         String text;
    #         if (saves.getSize() != 0) {
    #             text = NAME_LABEL + getMap().getTag();
    #         } else {
    #             text = "No Map Selected";
    #         }
    #         NAME_FIELD = new JLabel(text);
    #         NAME_FIELD.setBounds(0, TOP, PANEL_W, INPUT_H);
    #         add(NAME_FIELD);
    #     }

    def add_edit_map(self):
        None

    def add_run_map(self):
        None

    def add_prev(self):
        None

    def add_next(self):
        None

    def add_new_map(self):
        None
        # default map size:
        # this(new Map(PANE_W / Tile.PIXELS_PER_TILE + 1,
        #                      PANE_H / Tile.PIXELS_PER_TILE + 1));

    def add_select_map(self):
        None

#     /** MainPanel attributes */
#     private static final int NAME_Y        = TOP;
#     private static final int EDIT_Y        = NAME_Y + INPUT_H;
#     private static final int RUN_Y         = EDIT_Y + INPUT_H;
#     private static final int CYCLE_Y       = RUN_Y + INPUT_H;
#     private static final int SELECT_Y      = CYCLE_Y + INPUT_H;
#     private static final int CYCLE_W       = MIDDLE;
#     private static final String NAME_LABEL = "Name: ";
#     private JLabel NAME_FIELD;
#     private MapList saves;
#
#     /** MainPanel constructor */
#     MainPanel(MainMenu m) {
#         super(m);
#         saves = new MapList();
#         addNameLabel();
#         addEditButton();
#         addRunButton();
#         addPrevNextButtons();
#         addSelectButton();
#         addNewButton();
#         if (saves.getSize() != 0) {
#             setMap(saves.peek());
#         }
#     }
#
#     /** Populate the MainPanel with edit options */
#     private void addEditButton() {
#         addButton("Edit Map", 0, EDIT_Y, PANEL_W, INPUT_H,
#                 (ActionEvent a) -> {
#                     Map map = getMap();
#                     if (saves.getSize() != 0) {
#                         map.addListeners();
#                         changeScreen(new MakerMenu(map));
#                     }
#                 });
#     }
#
#     /** Populate the MainPanel with run options */
#     private void addRunButton() {
#         addButton("Run Map", 0, RUN_Y, PANEL_W, INPUT_H,
#                 (ActionEvent a) -> {
#                     Map map = getMap();
#                     if (saves.getSize() != 0) {
#                         changeScreen(new RunnerMenu(map));
#                     }
#                 });
#     }
#
#     /** Populate the MainPanel with prev & next options to cycle Maps */
#     private void addPrevNextButtons() {
#         addButton("<", 0, CYCLE_Y, CYCLE_W, INPUT_H,
#                 (ActionEvent a) -> {
#                     Map map = getMap();
#                     try {
#                         if (saves.getSize() != 0) {
#                             remove(map);
#                             map = saves.prev();
#                             setMap(map);
#                             updateFields();
#                         }
#                     } catch (Exception e) {
#                         e.printStackTrace();
#                     }
#                 });
#         addButton(">", MIDDLE, CYCLE_Y, CYCLE_W, INPUT_H,
#                 (ActionEvent a) -> {
#                     Map map = getMap();
#                     try {
#                         if (saves.getSize() != 0) {
#                             remove(map);
#                             map = saves.next();
#                             setMap(map);
#                             updateFields();
#                         }
#                     } catch (Exception e) {
#                         e.printStackTrace();
#                     }
#                 });
#     }
#
#     /** Populate the MainPanel with the option to select Map from directory */
#     private void addSelectButton() {
#         addButton("Select Map", 0, SELECT_Y, PANEL_W, INPUT_H,
#                 (ActionEvent a) -> {
#                     JFileChooser fileChooser = new JFileChooser(SAVE_DIR);
#                     int fileType = fileChooser.showOpenDialog(null);
#                     if (fileType == JFileChooser.APPROVE_OPTION) {
#                         File file = fileChooser.getSelectedFile();
#                         try {
#                             FileInputStream f = new FileInputStream(file);
#                             ObjectInputStream in = new ObjectInputStream(f);
#                             Map map = (Map) in.readObject();
#                             setMap(map);
#                         } catch (Exception e) {
#                             e.printStackTrace();
#                         }
#                     }
#                 });
#     }
#
#     /** Populate the MainPanel with the option to create a new Map */
#     private void addNewButton() {
#         addButton("New Map", 0, BOTTOM, PANEL_W, INPUT_H,
#                 (ActionEvent a) -> changeScreen(new MakerMenu()));
#     }
#
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
