from json import dump

from Panel import Panel
from Tile import Tile

from read_config import read_config

configs = read_config()
PANEL_W = configs["PANEL_W"]
SAVE_DIR = configs["SAVE_DIR"]
SAVE_EXT = configs["SAVE_EXT"]
ELEMENT_H = configs["ELEMENT_H"]
SET_WIDTH_Y = configs["SET_WIDTH_Y"]
SET_HEIGHT_Y = configs["SET_HEIGHT_Y"]
UPDATE_SIZE_W = configs["UPDATE_SIZE_W"]
SET_TERRAIN_H = configs["SET_TERRAIN_H"]
SET_TERRAIN_Y = configs["SET_TERRAIN_Y"]
NUM_CPUS_Y = configs["NUM_CPUS_Y"]
SAVE_Y = configs["SAVE_Y"]
NAME_Y = configs["NAME_Y"]
DEFAULT_TERRAIN = configs["DEFAULT_TERRAIN"]
MIDDLE = PANEL_W // 2

# MakerPanel class
class MakerPanel(Panel):

    # MakerPanel constructor
    def __init__(self, program, maker_menu):
        Panel.__init__(self, program, maker_menu)
        self.set_terrain_selection(DEFAULT_TERRAIN)

    # Getter method: terrain_selection
    def get_terrain_selection(self):
        return Tile.terrain_selection

    # Getter method: num_CPUs
    def get_num_CPUs(self):
        return self.num_CPUs.get()

    # Getter method: tag
    def get_tag(self):
        return self.tag.get()

    # Setter method: terrain_selection
    def set_terrain_selection(self, terrain_selection):
        Tile.terrain_selection = terrain_selection

    # Populate the MakerPanel with buttons
    def add_buttons(self):
        self.add_resize()
        self.add_set_terrain()
        self.add_num_CPUs()
        self.add_name()
        self.add_save()
        self.add_back()

    def add_resize(self):
        width_str = str(self.get_map().get_width())
        height_str = str(self.get_map().get_height())
        self.width_field = self.add_text_field("Width:", width_str,
                                               SET_WIDTH_Y, UPDATE_SIZE_W)
        self.height_field = self.add_text_field("Height:", height_str,
                                                SET_HEIGHT_Y, UPDATE_SIZE_W)
        def update_dimensions():
            try:
                new_width = self.width_field.get()
                new_height = self.height_field.get()
                self.get_map().set_size(new_width, new_height)
            except:
                print "Error in MakerPanel.add_resize"
        self.add_button("Update", PANEL_W - UPDATE_SIZE_W, SET_WIDTH_Y,
                        update_dimensions, UPDATE_SIZE_W, 2 * ELEMENT_H)

    def add_set_terrain(self):
        self.add_terrain_button("grass", 0, SET_TERRAIN_Y)
        self.add_terrain_button("gravel", MIDDLE, SET_TERRAIN_Y)
        self.add_terrain_button("road", 0, SET_TERRAIN_Y + SET_TERRAIN_H)
        self.add_terrain_button("ice", MIDDLE, SET_TERRAIN_Y + SET_TERRAIN_H)

    def add_terrain_button(self, terrain, x, y):
        set_terrain_type = lambda: self.set_terrain_selection(terrain)
        self.add_button(terrain, x, y, set_terrain_type, height=SET_TERRAIN_H, width=PANEL_W/2)

    def add_num_CPUs(self):
        CPUs_str = str(self.get_map().get_num_CPUs())
        self.num_CPUs = self.add_text_field("# CPUs:", CPUs_str, NUM_CPUS_Y)

    def add_name(self):
        self.tag = self.add_text_field("Name:", self.get_map().get_tag(), NAME_Y)

    def add_save(self):
        def save():
            map = self.get_map()
            map.set_num_CPUs(self.get_num_CPUs())
            map.set_tag(self.get_tag())
            filename = "{}{}{}".format(SAVE_DIR, map.get_tag(), SAVE_EXT)
            with open(filename, "w") as f:
                dump(map.__dict__, f)
        self.add_button("Save Map", 0, SAVE_Y, save)

# TODO: when you click on a car, that changes it's starting orientation.
# TODO: in the Runner, before it begins, a random variance gets added to each car's starting angle.

# TODO: see the revised Tile class on branch `natepy`
# TODO: since Tile no longer extends button, you need to bind every Tile to a key listener with [canvas].tag_bind(id, <binding>, command)

#     /** Change the dimensions of the Map */
#     private void changeMapSize(int width, int height) {
#         Map map                = getMap();
#         JScrollPane scrollPane = getPane();
#         map.setWidth(width);
#         map.setHeight(height);
#         scrollPane.updateUI();
#     }
#
#     /** Update fields in the MakerPanel after changing the Map */
#     void updateFields() {
#     }
