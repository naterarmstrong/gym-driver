from tkinter import *

if __name__ == '__main__':
    root = Tk()

from tkinter import ttk
from PIL import Image, ImageTk
import pygame as pg
import sys, os
import random
import time


from Tile import Tile
from Car import Car

from read_config import read_config

#configs = read_config()
#DEFAULT_NUM_CPUS = configs["DEFAULT_NUM_CPUS"]
#DEFAULT_TAG = configs["DEFAULT_TAG"]
#DEFAULT_START_ANGLE = configs["DEFAULT_START_ANGLE"]
#BACKGROUND_COLOR = configs["BACKGROUND_COLOR"]
#PIXELS_PER_TILE = configs["PIXELS_PER_TILE"]

DEFAULT_NUM_CPUS = 0
DEFAULT_TAG = None
DEFAULT_START_ANGLE = 0
BACKGROUND_COLOR = (25, 123, 48)
PIXELS_PER_TILE = 200

# Map class
class Map:

    # Map constructor
    def __init__(self, width, height, is_tkrendered=False, screen=None, canvas=None):
        self.width = width
        self.height = height
        self.tiles = []

        # Rendering / Screen creation logic
        # If is_tkrendered, renders to tk interface
        self.is_tkrendered = is_tkrendered
        self.screen = screen
        if self.is_tkrendered:
            self.set_canvas(canvas)
        # End rendering logic

        # Used/accessed by tile / car to edit properly
        self.set_currently_editing('path')


        # Tile Generation Logic
        for i in range(self.height):
            row = []
            for j in range(self.width):
                if self.is_tkrendered:
                    cur_canvas = self.get_canvas()
                    new_tile = Tile(self, canvas=cur_canvas, location=(j, i))
                    new_tile.render_to_canvas(j, i)
                    new_tile.add_listeners()
                else:
                    new_tile = Tile(self, canvas=None, location=(j, i))
                row.append(new_tile)
            self.tiles.append(row)
        self.set_num_CPUs(DEFAULT_NUM_CPUS)
        self.set_tag(DEFAULT_TAG)
        if self.tiles and self.tiles[0]:
            self.set_start_tile(self.tiles[0][0])
        else:
            self.set_start_tile(None)
        # End Tile Generation Logic

        self.cars = []

        self.set_start_angle(DEFAULT_START_ANGLE)
        # TODO: setLayout(null)

    # Add listeners to every Tile on the Map
    def add_listeners(self):
        for i in range(self.get_height()):
            row = self.tiles[i]
            for j in range(self.get_width()):
                tile = row[j]
                tile.add_listeners()

    # Getter method: currently_editing
    def get_currently_editing(self):
        return self.currently_editing

    def set_currently_editing(self, currently_editing):
        self.currently_editing = currently_editing

    # Getter method: width
    def get_width(self):
        return self.width

    # Getter method: height
    def get_height(self):
        return self.height

    # Getter method: num_CPUs
    def get_num_CPUs(self):
        return self.num_CPUs

    # Getter method: tag
    def get_tag(self):
        return self.tag

    # Getter method: start_tile
    def get_start_tile(self):
        return self.start_tile

    # Getter method: start_angle
    def get_start_angle(self):
        return self.start_angle

    # Getter method: Tile [provided (x, y) coordinate]
    def get_tile(self, x, y):
        x_tile = x // PIXELS_PER_TILE
        y_tile = y // PIXELS_PER_TILE
        return self.tiles[x_tile][y_tile]

    # Getter method: friction [provided (x, y) coordinate]
    def get_point_friction(self, x, y):
        x_pixel = x % PIXELS_PER_TILE
        y_pixel = y % PIXELS_PER_TILE
        return self.get_tile(x, y).get_point_friction(x_pixel, y_pixel)

    # Getter method: canvas
    def get_canvas(self):
        return self.canvas

    # Setter method: width
    def set_width(self, width):
        if width >= self.width:
            for row in self.tiles:
                for _ in range(width - self.width):
                    row.append(Tile(self))
        else:
            for row in self.tiles:
                for _ in range(self.width - width):
                    row.pop()
        self.width = width
        # TODO: render()

    # Setter method: height
    def set_height(self, height):
        if height >= self.height:
            for _ in range(height - self.height):
                row = [Tile(self) for _ in range(self.width)]
                self.tiles.append(row)
        else:
            for _ in range(self.height - height):
                self.tiles.pop()
        self.height = height
        # TODO: render()

    # Setter method: num_CPUs
    def set_num_CPUs(self, num_CPUs):
        self.num_CPUs = num_CPUs

    # Setter method: tag
    def set_tag(self, tag):
        self.tag = tag

    # Setter method: start_tile
    def set_start_tile(self, start_tile):
        self.start_tile = start_tile

    # Setter method: start_angle
    def set_start_angle(self, start_angle):
        self.start_angle = start_angle

    # Steps the map forward by 1 timestep
    def step(self, action):
        for car in self.cars:
            car.step(car_heuristic_func())
        main_car.step(action)

        # TODO: Actually return stuff
    
    # Renders everything to pygame properly
    def render_to_pygame(self, coords):
        self.screen.fill((25, 123, 48))
        for row in self.tiles:
            for tile in row:
                tile.render_to_pygame(self.screen, coords)
        for car in self.cars:
            car.render_to_pygame(self.screen, coords)
        #main_car.render_to_pygame(self.screen)
        pg.display.update()

    def test_pygame_movement(self, t):
        # runs for 10 seconds, .1 second per t
        self.render_to_pygame((t*5, t*5))
        time.sleep(.02)


    # Setter method: canvas
    def set_canvas(self, canvas):
        if canvas:
            self.canvas = canvas
        else:
            self.canvas = Canvas()

    def add_car(self, x, y):
        newcar = Car(self, x, y, 0, canvas=self.get_canvas())
        print "car created"
        newcar.render_to_canvas()
        print 'car rendered'
        self.cars.append(newcar)

    def get_currently_editing(self):
        return self.currently_editing


    def set_currently_editing(self, currently_editing):
        self.currently_editing = currently_editing

    # Sets the screen of the map (for pygame rendering)
    def set_screen(self, screen):
        self.screen = screen

    # Step

    # Reset

    # Render

    # TODO: putting cars on map, step, reset, render
    # TODO: in Robert's code, where it has `Canvas()`, just set that equal to the Map's canvas

if __name__ == "__main__":


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



    #images = Tile.terrain_images['road']['straight'][0]
    #canvas2.create_image(0, 0, image=images)



    tiles = []
    a = Map(5, 5, is_tkrendered=True, canvas=canvas2, screen=None)
    a.set_currently_editing('path')
    a.add_car(50, 50)
    #for x in range(5):
    #    for y in range(5):
    #        t = Tile(a, canvas=canvas2)
    #        t.render_to_canvas(x, y)
    #        t.add_listeners()
    #        tiles.append(t)


    #canvas2.itemconfigure(2, image=Tile.terrain_images['road']['quarter_turn'][180])
    


    
    #a = Map(3, 3, is_tkrendered=False, screen=screen)
    #a.render_to_pygame((0, 0))
    #for row in a.tiles:
    #    for tile in row:
    #        tile.cycle_path()
    #a.render_to_pygame((0, 0))
    #pg.display.update()
    counter = 0
    root.mainloop()

    pg.init()
    screen = pg.display.set_mode((512, 512))
    a.set_screen(screen)


    while counter < 300:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        a.test_pygame_movement(counter)
        print counter
        counter += 1
