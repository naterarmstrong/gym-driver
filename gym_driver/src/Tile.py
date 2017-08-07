from tkinter import * #TODO: CHANGE
from tkinter import ttk
from PIL import Image, ImageTk
import pygame as pg

import time
import random

#from Car import Car
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
# Checking if textures should be dictionary
TEXTURES = {
    'grass': .6,
    'ice': .1,
    'gravel': .5,
    'road': .9
    }
PATHS = ['straight', 'quarter_turn']
SCREEN_SIZE = 512



#TEST_IMAGE = ImageTk.PhotoImage(Image.open("../resources/straight_road_20.png"))

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

def populate_pg_terrain_images():
    # Exact same thing, but uses pygame image handling instead
    terrain_images = {}
    for texture in TEXTURES:
        terrain_images[texture] = {}
        for path in PATHS:
            terrain_images[texture][path] = {}
            cur_image = pg.image.load("../resources/{}_{}_{}.png".format(path, texture, PIXELS_PER_TILE))
            for orientation in ORIENTATIONS:
                terrain_images[texture][path][orientation] = \
                pg.transform.rotate(cur_image, orientation)
    return terrain_images
# Tile class
class Tile:

    # Tile class attributes
    terrain_selection = DEFAULT_TERRAIN
    pressed = False
    terrain_images = populate_terrain_images()
    pg_terrain_images = populate_pg_terrain_images()

    # Tile constructors
    def __init__(self, map, canvas=None, location=(0, 0), texture=DEFAULT_TERRAIN, path_ind=0, orientation=0):
        # Boolean flag to check if updates to visuals are needed
        self._rendered = False
        self.canvas = canvas
        self.set_map(map)
        self.set_texture(texture)
        self.set_path_ind(path_ind)
        self.set_orientation(orientation)
        self.location = location

        self.coords = (location[0]*PIXELS_PER_TILE, location[1]* PIXELS_PER_TILE)


    # Saves the tile into a python list of arguments to recreate the tile
    def save(self):
        location = self.location
        texture = self.get_texture()
        path_ind = self.path_ind
        orientation = self.get_orientation()
        return [location, texture, path_ind, orientation]


    # Populate the Tile with listeners to allow user interfacing
    def add_listeners(self):
        self.canvas.tag_bind(self.id, "<Enter>", self.on_enter)
        self.canvas.tag_bind(self.id, "<Button-1>", self.on_leftclick)
        self.canvas.tag_bind(self.id, "<Button-2>", self.on_rightclick)
        self.canvas.tag_bind(self.id, "<Key>", self.on_keypress)

    # Creates a rendered image at appropriate point on canvas
    def render_to_canvas(self, x, y):
        image = self.get_image('tk')
        id = self.canvas.create_image(self.calculate_placement(x), self.calculate_placement(y), image=image)
        self.id = id
        self._rendered = True


    # Called when changes are made to the tile. Updates the visual
    def update_canvas_render(self):
        if not self._rendered:
            return
        image = self.get_image('tk')
        self.canvas.itemconfigure(self.id, image=image)

    # Renders the tile to pygame. Location dependent on viewing window location
    def render_to_pygame(self, screen, screen_coords):
        image = self.get_image('pg')
        if -PIXELS_PER_TILE <= self.coords[0] - screen_coords[0] <= SCREEN_SIZE and \
            -PIXELS_PER_TILE <= self.coords[1] - screen_coords[1] <= SCREEN_SIZE:
            pos = (int(self.coords[0] - screen_coords[0]), int(self.coords[1] - screen_coords[1]))
            screen.blit(image, pos)
        else:
            pass

    # Gets the image of a tile, in either 'pg' or 'tk' format
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

    @staticmethod
    def calculate_placement(x):
        return (PIXELS_PER_TILE / 2) + PIXELS_PER_TILE * x


    def on_enter(self, event):
        # TODO: requestFocus()
        # TODO: Fix
        #if Tile.pressed:
        #    self.on_leftclick(event)
        pass

    def on_leftclick(self, event):
        #Tile.pressed = True
        #self.set_texture(Tile.terrain_selection)
        print self.map.get_currently_editing()
        currently_editing = self.map.get_currently_editing()
        #Tile.toggle_flag()
        if currently_editing == 'path':
            self.cycle_path()
        elif currently_editing == 'terrain':
            self.set_texture(Tile.terrain_selection)
        elif currently_editing == 'orientation':
            self.cycle_orientation()
        elif currently_editing == 'cars':
            self.map.add_car(event.x, event.y)
        else:
            print "Not currently editing anything"

    def on_rightclick(self, event):
        print 'Returning texture and friction'
        print self.map
        texture = self.get_point_texture(event.x % PIXELS_PER_TILE, event.y % PIXELS_PER_TILE)
        friction = self.map.get_point_friction(event.x, event.y)
        print texture, ' : ', friction
        

    def on_keypress(self, event):
        print "AYYY"
        char = event.char
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

    # Getter method: texture [given (x, y) coordinate] relative to tile
    def get_point_texture(self, x, y):
        path = self.get_path()
        texture = self.get_texture()
        if texture == 'grass': # for efficiency
            return 'grass'
        elif path == 'straight':
            return texture if self.in_straight_track(x, y) else 'grass'
        elif path == 'quarter_turn':
            return texture if self.in_quarter_turn(x, y) else 'grass'
        else:
            raise Exception("Unsupported path type")

    @staticmethod
    def in_circle(x, y, r):
        return x ** 2 + y ** 2 <= r ** 2


    # Returns if point is in a straight track
    # Assumes width of the track is 1/2 PIXELS_PER_TILE
    def in_straight_track(self, x, y):
        orientation = self.orientation
        if orientation == 0 or orientation == 180:
        # Horizontal straight track
            if PIXELS_PER_TILE / 4 <= y and PIXELS_PER_TILE * .75 >= y:
                return True
            else:
                return False
        elif orientation == 90 or orientation == 270:
            if PIXELS_PER_TILE / 4 <= x and PIXELS_PER_TILE * .75 >= x:
                return True
            else:
                return False


    # Returns if point is in a quarter turn
    # Assumes width of the track is 1/2 PIXELS_PER_TILE
    def in_quarter_turn(self, x, y):
        # Orientation defines a right hand turn, with the
        # right hand side along orientation. So a turn from
        # orientation-90 degree to orientation degrees
        orientation = self.get_orientation()
        if orientation == 0:
            newx, newy = PIXELS_PER_TILE - x, PIXELS_PER_TILE - y
        elif orientation == 90:
            newx, newy = PIXELS_PER_TILE - x, y
        elif orientation == 180:
            newx, newy = x, y
        elif orientation == 270:
            newx, newy = x, PIXELS_PER_TILE - y
        else:
            raise Exception("Unsupported orientation for a quarter turn")
        sq_dist = newx ** 2 + newy ** 2
        if sq_dist <= (PIXELS_PER_TILE ** 2) / 16 or \
        sq_dist >= (PIXELS_PER_TILE ** 2) * 9 / 16:
            return False
        else:
            return True

    # Getter method: path
    def get_path(self):
        return PATHS[self.path_ind]

    # Getter method: orientation
    def get_orientation(self):
        return self.orientation

    # Getter method: friction [provided texture]
    @staticmethod
    def get_texture_friction(texture):
        print texture
        return TEXTURES[texture]

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

    @staticmethod
    def set_terrain_selection(newterrain):
        if newterrain in TEXTURES:
            Tile.terrain_selection = newterrain

    @staticmethod
    def toggle_flag():
        if Tile.pressed:
            Tile.pressed = False
        else:
            Tile.pressed = True





#### TEST #####################
class TestingMap:
    def __init__(self):
        self.currently_editing = None
    def get_currently_editing(self):
        return self.currently_editing
    def set_currently_editing(self, currently_editing):
        self.currently_editing = currently_editing
    def add_car(self, x, y):
        b = Car(self, x, y, 0, canvas=canvas2)
        b.render_to_canvas()




if __name__ == '__main__':
    root = Tk()

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

    def edit_terrain(map):
        print "editing terrain"
        map.set_currently_editing('terrain')

    def edit_path(map):
        print "editing path"
        map.set_currently_editing('path')

    def edit_orientation(map):
        print "editing orientation"
        map.set_currently_editing('orientation')

    def edit_cars(map):
        print "editing cars"
        map.set_currently_editing('cars')


# BEGIN MAKESHIFT SIDEPANEL
    frame = ttk.Frame(root)
    frame.grid(column=1, row=0, sticky=(N, S, E))
    cars_button = ttk.Button(frame, text="Add Cars", command = lambda : edit_cars(a))
    cars_button.grid(column=0, row=2)
    terrain_button = ttk.Button(frame, text="Change Terrain", command=lambda : edit_terrain(a))
    terrain_button.grid(column=0, row=3)
    path_button = ttk.Button(frame, text="Change Path", command=lambda : edit_path(a))
    path_button.grid(column=0, row=4)
    orientation_button = ttk.Button(frame, text="Change Orientation", command=lambda : edit_orientation(a))
    orientation_button.grid(column=0, row=5)
    choices_label = ttk.Label(frame, text="Available terrain")
    choices_label.grid(column=0, row=6)
    choice_grass = ttk.Button(frame, text="grass", command=lambda: Tile.set_terrain_selection('grass'))
    choice_grass.grid(column=0, row=7)
    choice_road = ttk.Button(frame, text="road", command=lambda: Tile.set_terrain_selection('road'))
    choice_road.grid(column=0, row=8)
    choice_gravel = ttk.Button(frame, text="gravel", command=lambda: Tile.set_terrain_selection('gravel'))
    choice_gravel.grid(column=0, row=9)
    choice_ice = ttk.Button(frame, text="ice", command=lambda: Tile.set_terrain_selection('ice'))
    choice_ice.grid(column=0, row=10)
    #### END MAKESHIFT SIDEPANEL

    canvas2.bind("<Enter>", lambda event: canvas2.focus_set())



    images = Tile.terrain_images['road']['straight'][0]
    canvas2.create_image(0, 0, image=images)

    tiles = []
    a = TestingMap()
    a.set_currently_editing('path')
    for x in range(5):
        for y in range(5):
            t = Tile(a, canvas=canvas2)
            t.render_to_canvas(x, y)
            t.add_listeners()
            tiles.append(t)


    #canvas2.itemconfigure(2, image=Tile.terrain_images['road']['quarter_turn'][180])
    root.mainloop()

