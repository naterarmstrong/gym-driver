import sys, os
import random
import time

from tkinter import *
if __name__ == '__main__':
    root = Tk()
from tkinter import ttk
from PIL import Image, ImageTk
import pygame as pg
import numpy as np


from Tile import Tile
from Car import Car
from PointCar import PointCar
from KinematicCar import KinematicCar
from DynamicCar import DynamicCar
from Controller import Controller # TODO: MOVE
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
SCREEN_SIZE = 512

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
        self.main_car = None

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
        print x
        print type(x)
        print '---------------'
        x_tile = int(x) // PIXELS_PER_TILE
        y_tile = int(y) // PIXELS_PER_TILE
        return self.tiles[y_tile][x_tile]

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
            pass
            #car.step(car_heuristic_func())
        # Action from controller currently intended to look into the discretized
        acc, steer = action
        acc = acc*3.0 - 3.0
        steer = steer*15.0 - 15.0
        self.main_car.step((acc, steer))
        x = self.main_car.x
        y = self.main_car.y
        #angle = np.radians(self.main_car.get_angle())
        coords = (x + (SCREEN_SIZE / 2), y + (SCREEN_SIZE / 2))
        # TODO: convert action to the state space
        self.render_to_pygame(coords)

        # TODO: Actually return stuff
    
    # Renders everything to pygame properly
    def render_to_pygame(self, coords):
        self.screen.fill((25, 123, 48))
        for row in self.tiles:
            for tile in row:
                tile.render_to_pygame(self.screen, coords)
        for car in self.cars:
            car.render_to_pygame(self.screen, coords)
        main_car.render_to_pygame(self.screen, coords)
        pg.display.update()


    # Setter method: canvas
    def set_canvas(self, canvas):
        if canvas:
            self.canvas = canvas
            canvas.bind("<ButtonRelease-1>", lambda _: Tile.toggle_flag())
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

    # Sets the main car of the map to be a car
    def set_main_car(self, car):
        self.main_car = car

    def get_main_car(self):
        if self.main_car:
            return self.main_car
        else:
            raise Exception("No main car exists")

    # Reset

    # Render

    # TODO: putting cars on map, step, reset, render
    # TODO: in Robert's code, where it has `Canvas()`, just set that equal to the Map's canvas

if __name__ == "__main__":


    h = ttk.Scrollbar(root, orient=HORIZONTAL)
    v = ttk.Scrollbar(root, orient=VERTICAL)
    canvas2 = Canvas(root, scrollregion=(0, 0, 5000, 5000), yscrollcommand=v.set, xscrollcommand=h.set)
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
    a = Map(25, 25, is_tkrendered=True, canvas=canvas2, screen=None)
    a.set_currently_editing('path')
    main_car = DynamicCar(a, 250, 300, 0, canvas2)
    a.set_main_car(main_car)
    main_car.render_to_canvas()
    


    

    for row in a.tiles:
        for tile in row:
            if random.random() > .5:
                tile.cycle_path()
            if random.random() > .5:
                tile.cycle_orientation()
    #a.render_to_pygame((0, 0))
    #pg.display.update()
    counter = 0
    root.mainloop()

    pg.init()
    screen = pg.display.set_mode((512, 512))
    a.set_screen(screen)

    controller = Controller()
    clock = pg.time.Clock()



    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        action = controller.process_input(a)
        a.step(action)
        #main_car.render_to_pygame(screen, (500, 500))
        pg.display.update()
        clock.tick(30)
        print counter
        counter += 1
