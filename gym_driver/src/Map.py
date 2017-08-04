from tkinter import Canvas
from PIL import Image, ImageTk
import pygame as pg
import sys, os


from Tile import Tile

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
    def __init__(self, width, height, is_tkrendered=False, screen=None):
        self.width = width
        self.height = height
        self.tiles = []

        # Rendering / Screen creation logic
        # If is_tkrendered, renders to tk interface
        self.is_tkrendered = is_tkrendered
        self.screen = screen
        if self.is_tkrendered:
            self.set_canvas(Canvas())
        # End rendering logic


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
        self.render_to_pygame((0, 0))

    # Add listeners to every Tile on the Map
    def add_listeners(self):
        for i in range(self.get_height()):
            row = self.tiles[i]
            for j in range(self.get_width()):
                tile = row[j]
                tile.add_listeners()

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
            car.render_to_pygame(self.screen)
        #main_car.render_to_pygame(self.screen)
        pg.display.update()


    # Setter method: canvas
    def set_canvas(self, canvas):
        self.canvas = canvas

    # Step

    # Reset

    # Render

    # TODO: putting cars on map, step, reset, render
    # TODO: in Robert's code, where it has `Canvas()`, just set that equal to the Map's canvas

if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode((512, 512))
    a = Map(3, 3, is_tkrendered=False, screen=screen)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
