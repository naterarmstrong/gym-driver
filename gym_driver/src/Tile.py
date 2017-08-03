from tkinter import * #TODO: CHANGE
from tkinter import ttk
from PIL import Image, ImageTk

import time

from read_config import read_config

#configs = read_config()
#PIXELS_PER_TILE = configs["PIXELS_PER_TILE"]
#DEFAULT_TERRAIN = configs["DEFAULT_TERRAIN"]
#TEXTURES = configs["TEXTURES"]
#PATHS = configs["PATHS"]
ORIENTATIONS = [0, 90, 180, 270]

# Below commented out config sections are for testing only
###TODO: REMOVE
PIXELS_PER_TILE = 200
DEFAULT_TERRAIN = 'road'
TEXTURES = ['grass', 'ice', 'gravel', 'road']
PATHS = ['straight', 'quarter_turn']

root = Tk()

TEST_IMAGE = ImageTk.PhotoImage(Image.open("../resources/straight_road_200.png"))

def populate_terrain_images():
    # It's really ugly, but Tk has super weird scoping issues
    # They are avoided by definiing all PhotoImages in the global frame, I think
    # Only mess with this if brave and patient
    terrain_images = {}
    for texture in TEXTURES:
        terrain_images[texture] = {}
        for path in PATHS:
            terrain_images[texture][path] = {}
            cur_image = Image.open("../resources/{}_{}_{}.png".format(path, texture, PIXELS_PER_TILE))
            for orientation in ORIENTATIONS:
                terrain_images[texture][path][orientation] = \
                ImageTk.PhotoImage(cur_image.rotate(orientation))
    return terrain_images

# Tile class
class Tile:

    # Tile class attributes
    terrain_selection = DEFAULT_TERRAIN
    pressed = False
    terrain_images = populate_terrain_images()

    # Tile constructors
    def __init__(self, map, canvas=None, texture=DEFAULT_TERRAIN, path_ind=0, orientation=0):
        # Boolean flag to check if updates to visuals are needed
        self._rendered = False
        self.canvas = canvas
        #self.set_map(map)
        self.set_texture(texture)
        self.set_path_ind(path_ind)
        self.set_orientation(orientation)
        # TODO: setBackground(getColor(texture));
        #self.add_listeners()

    # Populate the Tile with listeners to allow user interfacing
    def add_listeners(self):
        self.canvas.tag_bind(self.id, "<Enter>", self.on_enter)
        self.canvas.tag_bind(self.id, "<Button-1>", self.on_leftclick)
        self.canvas.tag_bind(self.id, "<Button-2>", self.on_rightclick)
        self.canvas.tag_bind(self.id, "<Key>", self.on_keypress)

    # Creates a rendered image at appropriate point on canvas
    def render_to_canvas(self, x, y):
        texture = self.get_texture()
        path = self.get_path()
        orientation = self.get_orientation()
        image = Tile.terrain_images[texture][path][orientation]
        id = self.canvas.create_image(self.calculate_placement(x), self.calculate_placement(y), image=image)
        self.id = id
        self._rendered = True


    # Called when changes are made to the tile. Updates the visual
    def update_canvas_render(self):
        if not self._rendered:
            return
        texture = self.get_texture()
        path = self.get_path()
        orientation = self.get_orientation()
        image = Tile.terrain_images[texture][path][orientation]
        self.canvas.itemconfigure(self.id, image=image)

    @staticmethod
    def calculate_placement(x):
        return (PIXELS_PER_TILE / 2) + PIXELS_PER_TILE * x


    def on_enter(self, event):
        # TODO: requestFocus()
        # TODO: Fix
        if Tile.pressed:
            self.set_texture(Tile.terrain_selection)

    def on_leftclick(self, event):
        #Tile.pressed = True
        #self.set_texture(Tile.terrain_selection)
        print Tile.terrain_selection
        self.cycle_path()

    def on_rightclick(self, event):
        self.cycle_orientation()

    def on_keypress(self, event):
        print "AYYY"
        char = event.char
        print char
        if char == "r":
            self.cycle_orientation()
        elif char == "g":
            self.set_texture("gravel")
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
        #TODO:: FIX
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
            if self.get_texture() == DEFAULT_TERRAIN:
                self.set_path_ind(0)
            self.update_canvas_render()

    # Setter method: path_ind
    def set_path_ind(self, path_ind):
        self.path_ind = path_ind

    # Setter method: orientation
    def set_orientation(self, orientation):
        self.orientation = orientation

    # Cycle to the next path type
    def cycle_path(self):
        self.set_path_ind((self.path_ind + 1) % len(PATHS))
        self.update_canvas_render()

    # Cycle to the next orientation
    def cycle_orientation(self):
        self.set_orientation((self.orientation + 90) % 360)
        self.update_canvas_render()

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

#### TEST
h = ttk.Scrollbar(root, orient=HORIZONTAL)
v = ttk.Scrollbar(root, orient=VERTICAL)
canvas2 = Canvas(root, scrollregion=(0, 0, 1000, 1000), yscrollcommand=v.set, xscrollcommand=h.set)
h['command'] = canvas2.xview
v['command'] = canvas2.yview
ttk.Sizegrip(root).grid(column=10, row=10, sticky=(S,E))

canvas2.grid(column=0, row=0, sticky=(N,W,E,S))
h.grid(column=0, row=10, sticky=(W,E))
v.grid(column=10, row=0, sticky=(N,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

canvas2.bind("<Enter>", lambda event: canvas2.focus_set())
def terrain_changer(event):
    char = event.char
    if char == 'g':
        Tile.terrain_selection == 'gravel'
    elif char == 'i':
        Tile.terrain_selection == 'ice'

canvas2.bind("<Key>", terrain_changer)


#images = Tile.terrain_images['road']['straight']
#images = ImageTk.PhotoImage(images)
#canvas2.create_image(0, 0, image=images)

for x in range(3):
    for y in range(3):
        t = Tile(None, canvas=canvas2)
        t.render_to_canvas(x, y)
        t.add_listeners()


#canvas2.itemconfigure(2, image=Tile.terrain_images['road']['quarter_turn'][180])
root.mainloop()

