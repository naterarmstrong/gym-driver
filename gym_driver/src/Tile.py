from PIL import Image, ImageTk
from pygame import image, transform

from read_config import read_config

configs = read_config()
PIXELS_PER_TILE = configs["PIXELS_PER_TILE"]
DEFAULT_TERRAIN = configs["DEFAULT_TERRAIN"]
TEXTURES = configs["TEXTURES"]
PATHS = configs["PATHS"]
ORIENTATIONS = configs["ORIENTATIONS"]

# TODO: Make the colors make sense in each tile png. (road = dark grey, gravel = brown, ice = blue-white)

# Tile class
class Tile:

    # Tile class attributes
    pressed = False
    imgs_computed_TODO_fix = False

    # Tile constructors
    def __init__(self, map, x, y, texture=DEFAULT_TERRAIN, path_ind=0, orientation=0):
        self.x, self.y = x, y
        self.set_path_ind(path_ind)
        self.set_orientation(orientation)
        self.set_map(map)
        self.root = self.map.program.root
        if not self.imgs_computed_TODO_fix:
            Tile.imgs_computed_TODO_fix = True
            Tile.terrain_images = self.populate_terrain_images()
            Tile.pg_terrain_images = self.populate_terrain_images()
        self.set_texture(texture)

        self.tk_render(x, y)
        # self.add_listeners()

    # Populate the Tile with listeners to allow user interfacing
    def add_listeners(self):
        canvas = self.map.get_canvas()
        canvas.tag_bind(self.id, "<Enter>", self.on_enter)
        canvas.tag_bind(self.id, "<ButtonPress-1>", self.on_leftclick)
        canvas.tag_bind(self.id, "<ButtonRelease-1>", self.on_leftrelease)
        canvas.tag_bind(self.id, "<Button-2>", self.on_rightclick)
        canvas.tag_bind(self.id, "<Key>", self.on_keypress)

    def on_enter(self, event):
        # TODO: requestFocus()
        print Tile.pressed
        if Tile.pressed:
            self.on_leftclick(event)

    def on_leftclick(self, event):
        Tile.pressed = True
        self.set_texture(Tile.terrain_selection)

    def on_leftrelease(self, event):
        Tile.pressed = False

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

    # Get the image of a tile, in either 'pg' or 'tk' format TODO fix
    def get_image(self, image_format):
        texture = self.get_texture()
        path = self.get_path()
        orientation = self.get_orientation()
        if image_format == 'tk':
            image = Tile.terrain_images[texture][path][orientation]
        elif image_format == 'pg':
            image = Tile.pg_terrain_images[texture][path][orientation]
        else:
            raise Exception("Image format {} not supported".format(image_format))
        return image

    # Setter method: map
    def set_map(self, map):
        self.map = map

    # Setter method: texture
    def set_texture(self, texture):
        if texture in TEXTURES:
            self.texture = texture
            self.tk_render(self.x, self.y)
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

    # Render the Tile in Tkinter
    def tk_render(self, x, y):
        image = self.get_image('tk')
        self.id = self.map.get_canvas().create_image(self.calculate_placement(x), self.calculate_placement(y), image=image)
        self.add_listeners()

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

    @staticmethod
    def populate_terrain_images():
        # It's really ugly, but Tk has super weird scoping issues
        # They are avoided by definiing all PhotoImages in the global frame, I think
        # Only mess with this if brave and patient
        terrain_images = {}
        for texture in TEXTURES:
            terrain_images[texture] = {}
            for path in PATHS:
                terrain_images[texture][path] = {}
                cur_image = Image.open(
                    "../resources/{}_{}_{}.png".format(path, texture,
                                                       PIXELS_PER_TILE))
                for orientation in ORIENTATIONS:
                    terrain_images[texture][path][orientation] = \
                        ImageTk.PhotoImage(cur_image.rotate(orientation))
        return terrain_images

    @staticmethod
    def populate_pg_terrain_images():
        # Exact same thing, but uses pygame image handling instead
        terrain_images = {}
        for texture in TEXTURES:
            terrain_images[texture] = {}
            for path in PATHS:
                terrain_images[texture][path] = {}
                cur_image = image.load(
                    "../resources/{}_{}_{}.png".format(path, texture,
                                                       PIXELS_PER_TILE))
                for orientation in ORIENTATIONS:
                    terrain_images[texture][path][orientation] = \
                        transform.rotate(cur_image, orientation)
        return terrain_images

    @staticmethod
    def calculate_placement(x):
        return (PIXELS_PER_TILE / 2) + PIXELS_PER_TILE * x
