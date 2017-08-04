from pickle import dump

from Panel import Panel

from read_config import read_config

configs = read_config()
SAVE_DIR = configs["SAVE_DIR"]
SAVE_EXT = configs["SAVE_EXT"]
DEFAULT_TERRAIN = configs["DEFAULT_TERRAIN"]
PANEL_W = configs["PANEL_W"]
ELEMENT_H = configs["ELEMENT_H"]
RESIZE_Y = configs["RESIZE_Y"]
CHNG_TERRAIN_Y = configs["CHNG_TERRAIN_Y"]
NUM_CPUS_Y = configs["NUM_CPUS_Y"]
TAG_Y = configs["TAG_Y"]
SAVE_Y = configs["SAVE_Y"]
UPDATE_W = configs["UPDATE_W"]
CHNG_TERRAIN_H = configs["CHNG_TERRAIN_H"]
MIDDLE = PANEL_W // 2

# MakerPanel class
class MakerPanel(Panel):

    # MakerPanel constructor
    def __init__(self, program, maker_menu):
        Panel.__init__(self, program, maker_menu)
        self.set_terrain_selection(DEFAULT_TERRAIN)

    # Getter method: terrain_selection
    def get_terrain_selection(self):
        return self.terrain_selection

    # Getter method: num_CPUs
    def get_num_CPUs(self):
        return self.num_CPUs.get()

    # Getter method: tag
    def get_tag(self):
        return self.tag.get()

    # Setter method: terrain_selection
    def set_terrain_selection(self, terrain_selection):
        self.terrain_selection = terrain_selection

    # Populate the MakerPanel with buttons
    def add_buttons(self):
        self.add_resize()
        self.add_chng_terrain()
        self.add_num_CPUs()
        self.add_tag()
        self.add_save()
        self.add_back()

    def add_resize(self):
        width_str = str(self.get_map().get_width())
        height_str = str(self.get_map().get_height())
        self.width_field = self.add_text_field("Width:", width_str, RESIZE_Y)
        self.height_field = self.add_text_field("Height:", height_str, RESIZE_Y)
        def update_dimensions():
            try:
                new_width = self.width_field.get()
                new_height = self.height_field.get()
                self.get_map().set_size(new_width, new_height)
            except:
                print "Invalid dimensions"
        self.add_button("Update", PANEL_W - UPDATE_W, RESIZE_Y,
                        update_dimensions, UPDATE_W, 2 * ELEMENT_H)

    def add_chng_terrain(self):
        self.add_terrain_button("grass", 0, CHNG_TERRAIN_Y)
        self.add_terrain_button("gravel", MIDDLE, CHNG_TERRAIN_Y)
        self.add_terrain_button("road", 0, CHNG_TERRAIN_Y + CHNG_TERRAIN_H)
        self.add_terrain_button("ice", MIDDLE, CHNG_TERRAIN_Y + CHNG_TERRAIN_H)

    def add_terrain_button(self, terrain, x, y):
        chng_terrain_type = lambda: self.set_terrain_selection(terrain)
        self.add_button(terrain, x, y, chng_terrain_type, height=CHNG_TERRAIN_H, width=PANEL_W/2)

    def add_num_CPUs(self):
        CPUs_str = str(self.get_map().get_num_CPUs())
        self.num_CPUs = self.add_text_field("Num CPUs:", CPUs_str, NUM_CPUS_Y)

    def add_tag(self):
        self.tag = self.add_text_field("Name:", self.get_map().get_tag(), TAG_Y)

    def add_save(self):
        def save():
            map = self.get_map()
            map.set_num_CPUs(self.get_num_CPUs())
            map.set_tag(self.get_tag())
            save_dir = "{}/{}{}".format(SAVE_DIR, map.get_tag(), SAVE_EXT)
            with open(save_dir, "w") as f:
                dump(map, f)
        self.add_button("Save Map", 0, SAVE_Y, save)

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