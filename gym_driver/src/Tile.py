from read_config import read_config

configs = read_config()
PIXELS_PER_TILE = configs["PIXELS_PER_TILE"]
DEFAULT_TERRAIN = configs["DEFAULT_TERRAIN"]
TEXTURES = configs["TEXTURES"]
PATHS = configs["PATHS"]
ORIENTATIONS = configs["ORIENTATIONS"]

# Tile class
class Tile:

    # Tile class attributes
    terrain_selection = DEFAULT_TERRAIN
    pressed = False

    # Tile constructors
    def __init__(self, map, texture=DEFAULT_TERRAIN, path_ind=0, orientation=0):
        self.set_map(map)
        self.set_texture(texture)
        self.set_path_ind(path_ind)
        self.set_orientation(orientation)
        self.add_listeners()

    # Populate the Tile with listeners to allow user interfacing
    def add_listeners(self):
        self.bind("<Enter>", self.on_enter)
        self.bind("<Button-1>", self.on_leftclick)
        self.bind("<Button-2>", self.on_rightclick)
        self.bind("<Key>", self.on_keypress)

    def on_enter(self, event):
        # TODO: requestFocus()
        if Tile.pressed:
            self.set_texture(Tile.terrain_selection)

    def on_leftclick(self, event):
        Tile.pressed = True
        self.set_texture(Tile.terrain_selection)

    def on_rightclick(self, event):
        self.cycle_path()

    def on_keypress(self, event):
        char = event.char
        if char == "r":
            self.cycle_orientation()
        elif char == "w":
            self.map.set_start_angle(90)
        elif char == "a":
            self.map.set_start_angle(180)
        elif char == "s":
            self.map.set_start_angle(270)
        elif char == "d":
            self.map.set_start_angle(0)
        # TODO: self.repaint()

    # Getter method: texture
    def get_texture(self):
        return self.texture

    # Getter method: texture [given (x, y) coordinate]
    def get_point_texture(self, x, y):
        path = self.get_path()
        if path == "flat":
            return self.get_texture()
        else:
            orientation = self.get_orientation()
            if orientation == 0:
                in_circle = self.in_circle(x, y - PIXELS_PER_TILE)
            elif orientation == 90:
                in_circle = self.in_circle(x - PIXELS_PER_TILE, y - PIXELS_PER_TILE)
            elif orientation == 180:
                in_circle = self.in_circle(x - PIXELS_PER_TILE, y)
            elif orientation == 270:
                in_circle = self.in_circle(x, y)
            else:
                raise Exception("Unsupported orientation")
            if path == "convex":
                return self.get_texture() if in_circle else DEFAULT_TERRAIN
            elif path == "concave":
                return DEFAULT_TERRAIN if in_circle else self.get_texture()
            else:
                raise Exception("Unsupported path type")

    @staticmethod
    def in_circle(x, y):
        return x * x + y * y <= PIXELS_PER_TILE * PIXELS_PER_TILE

    # Getter method: path
    def get_path(self):
        return PATHS[self.path_ind]

    # Getter method: orientation
    def get_orientation(self):
        return self.orientation

    # Getter method: friction [provided texture]
    @staticmethod
    def get_texture_friction(texture):
        return TEXTURES[texture][0]

    # Getter method: friction [provided (x, y) coordinate]
    def get_point_friction(self, x, y):
        texture = self.get_point_texture(x, y)
        return Tile.get_texture_friction(texture)

    # Setter method: map
    def set_map(self, map):
        self.map = map

    # Setter method: texture
    def set_texture(self, texture):
        if texture in TEXTURES:
            self.texture = texture
            # TODO: setBackground(getColor(texture))
            if self.get_texture() == DEFAULT_TERRAIN:
                self.set_path_ind(0)

    # Setter method: path_ind
    def set_path_ind(self, path_ind):
        self.path_ind = path_ind

    # Setter method: orientation
    def set_orientation(self, orientation):
        self.orientation = orientation

    # Cycle to the next path type
    def cycle_path(self):
        if self.get_texture() != DEFAULT_TERRAIN:
            self.set_path_ind((self.path_ind + 1) % len(PATHS))
            # TODO: paint(getGraphics());

    # Cycle to the next orientation
    def cycle_orientation(self):
        path = self.get_path()
        if path == "convex" or path == "concave":
            self.set_orientation((self.orientation + 90) % 360)

    # TODO
    #     /** Draw the Tile */
    #     @Override
    #     public void paint(Graphics g) {
    #         super.paintComponent(g);
    #         for (int i = 0; i < PIXELS_PER_TILE; i += 1) {
    #             for (int j = 0; j < PIXELS_PER_TILE; j += 1) {
    #                 String texture = getPtTextureInd(i, j);
    #                 Color color = getColor(texture);
    #                 g.setColor(color);
    #                 g.fillRect(i, j, 1, 1);
    #             }
    #         }
    #         if (this == map.getStartTile()) {
    #             int x = PIXELS_PER_TILE / 2;
    #             int y = PIXELS_PER_TILE / 2;
    #             g.setColor(Color.ORANGE);
    #             switch (map.getStartAngle()) {
    #                 case 0:
    #                     g.drawString("\u25BA", x, y);
    #                     break;
    #                 case 90:
    #                     g.drawString("\u25B2", x, y);
    #                     break;
    #                 case 180:
    #                     g.drawString("\u25C4", x, y);
    #                     break;
    #                 case 270:
    #                     g.drawString("\u25BC", x, y);
    #                     break;
    #             }
    #         }
    #     }
    #
    # }
