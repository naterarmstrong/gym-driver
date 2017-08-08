import sys, os
import random
import time
import json

from tkinter import *
if __name__ == '__main__':
    root = Tk()
from tkinter import ttk
from PIL import Image, ImageTk
import pygame as pg
import numpy as np
import cv2


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
DOWNSAMPLED_SIZE = 64
# Action space is discrete, acceleration, steering
# each of acc and steering is min, max, num of choices
ACTION_SPACE = ['discrete', [-2.0, 2.0, 3], [-30.0, 30.0, 5]]
STATE_SPACE = 'images'
DOWNSAMPLED_SIZE = 64

# Map class
class Map:

    # Map constructor
    # If map_dict is not none, then it will load everything from map_dict instead
    def __init__(self, width=6, height=6, is_tkrendered=False, screen=None, canvas=None, map_dict=None):
        
        self.width = width
        self.height = height
        self.tiles = []

        # Rendering / Screen creation logic
        # If is_tkrendered, renders to tk interface
        self.is_tkrendered = is_tkrendered
        self.screen = screen
        if self.is_tkrendered:
            self.set_canvas(canvas)
        else:
            self.set_canvas(None)
        # End rendering logic

        # Used/accessed by tile / car to edit properly
        self.set_currently_editing('path')

        # Creating Action Space
        self.create_action_space()


        if not map_dict:
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
            # End Tile Generation Logic

            self.cars = []
            self.main_car = None

            self.set_start_angle(DEFAULT_START_ANGLE)
        # To load from an existing map dict file
        else:
            # Tile Generation
            self.tiles = []
            self.height = len(map_dict['tiles'])
            self.width = len(map_dict['tiles'][0])
            for i in range(self.height):
                row = []
                for j in range(self.width):
                    #TODO: Account for not rendering to Tk
                    tile_params = map_dict['tiles'][i][j]
                    # Params are location, texture, path_ind, orientation
                    location = tile_params[0]
                    texture = tile_params[1]
                    path_ind = tile_params[2]
                    orientation = tile_params[3]
                    cur_canvas = self.get_canvas()
                    new_tile = Tile(self, canvas=cur_canvas, location=location, texture=texture, \
                        path_ind=path_ind, orientation=orientation)
                    new_tile.render_to_canvas(location[0], location[1])
                    new_tile.add_listeners()
                    row.append(new_tile)
                self.tiles.append(row)
            # End Tile Generation

            # Car Generation
            self.cars = []
            main_car_params = map_dict['main_car']
            # Those are x, y, angle, color
            x = main_car_params[0]
            y = main_car_params[1]
            angle = main_car_params[2]
            color = main_car_params[3]
            # TODO: Make it learn what type of car the main car is
            self.main_car = DynamicCar(self, x, y, angle, canvas=self.get_canvas(), color=color)
            if self.get_canvas():
                self.main_car.render_to_canvas()


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
        x_tile = int(x) // PIXELS_PER_TILE
        y_tile = int(y) // PIXELS_PER_TILE
        return self.tiles[y_tile][x_tile]

    # Getter method: friction [provided (x, y) coordinate]
    def get_point_friction(self, x, y):
        if x // PIXELS_PER_TILE >= self.width or y // PIXELS_PER_TILE >= self.height:
            return .6
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

    # Initializes an action space to get actions
    def create_action_space(self):
        action_space_type, acc_space_params, steer_space_params = ACTION_SPACE
        self.action_space_type = action_space_type
        if action_space_type == 'discrete':
            # Acceleration and Steer Space
            self.acc_space = np.linspace(*acc_space_params)
            self.steer_space = np.linspace(*steer_space_params)
        elif action_space_type == 'continuous':
            pass # TODO: FIX
        else:
            raise NotImplementedError

    # Converts an action into the action space
    # Prints out 'outside of range' if the action is outside the range of the action space
    def convert_to_action_space(self, action):
        if self.action_space_type == 'discrete':
            try:
                acc = self.acc_space[action[0]]
                steer = self.steer_space[action[1]]
                return (acc, steer)
            except IndexError as e:
                print 'Action outside of range: {}'.format(action)
        elif self.action_space_type == 'continuous':
            pass
        else:
            raise Exception("Unimplemented action space type: {}".format(self.action_space_type))

    # Steps the map forward by 1 timestep
    def step(self, action):
        for car in self.cars:
            car.step(self.car_heuristic_func(car))
        action = self.convert_to_action_space(action)
        self.main_car.step(action)
        x = self.main_car.x
        y = self.main_car.y
        coords = (x - (SCREEN_SIZE / 2), y - (SCREEN_SIZE / 2))
        self.render_to_pygame(coords)

        # TODO: Actually return stuff
        observation = self.get_observation()
        print observation

    # Steps ahead the simulation 

    def lookahead(self, action):
        for car in self.cars:
            car.step(self.car_heuristic_func(car))
        action = self.convert_to_action_space(action)
        self.main_car.step(action)


    # Gets an observation from the current state (the screen must already be updated)
    def get_observation(self):
        print STATE_SPACE
        if STATE_SPACE == 'images':
            image = pg.surfarray.array2d(self.screen).astype(np.uint8)
            downsampled_img = self.downsample(image)
        else:
            raise NotImplementedError

    # Downsamples an image using OpenCV's implementation
    # The image array is an np.uint8
    def downsample(self, image_array):
        width, height = image_array.shape
        if DOWNSAMPLED_SIZE is not None:
            while width > DOWNSAMPLED_SIZE and height > DOWNSAMPLED_SIZE:
                image_array = cv2.pyrDown(image_array, dstsize = (width / 2, height / 2))
                width, height = image_array.shape
        return image_array


    # Gives an action to move the cars heuristically
    # TODO: Do
    def car_heuristic_func(car):
        pass
    
    # Renders everything to pygame properly
    def render_to_pygame(self, coords):
        self.screen.fill((25, 123, 48))
        for row in self.tiles:
            for tile in row:
                tile.render_to_pygame(self.screen, coords)
        for car in self.cars:
            car.render_to_pygame(self.screen, coords)
        self.main_car.render_to_pygame(self.screen, coords)
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


    # Save map to a JSON filepath
    def save(self, filepath):
        map_dict = {}
        # Saving data about the map itself
        # Saving Tiles
        map_dict['tiles'] = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                saved_tile = self.tiles[y][x].save()
                row.append(saved_tile)
            map_dict['tiles'].append(row)
        # Saving Cars
        map_dict['cars'] = []
        for car in self.cars:
            saved_car = car.save()
            map_dict['cars'].append(saved_car)
        # Saving main car
        map_dict['main_car'] = self.main_car.save()

        json.dump(map_dict, open(filepath, 'w'), indent=4)

        print "Saved at {}".format(filepath)


    # Saves the state of the cars in the map
    # Intended for use before running the simulator
    def set_initial_state(self):
        self.initial_state = self.save_state()

    # Intended for use by supervisor agent, saves state
    def save_state(self):
        saved_state = {}
        saved_state['cars'] = []
        for car in self.cars:
            saved_car = car.save()
            saved_state['cars'].append(saved_car)
        saved_state['main_car'] = self.main_car.save()
        return saved_state

    # Takes in a state (in terms of cars), loads map to that point
    def load_to_state(self, state):
        main_car_params = state['main_car']
        # Those are x, y, angle, color
        x = main_car_params[0]
        y = main_car_params[1]
        angle = main_car_params[2]
        color = main_car_params[3]
        self.main_car = DynamicCar(self, x, y, angle, canvas=self.get_canvas(), color=color)
        self.cars = []
        for car_params in state['cars']:
            x = car_params[0]
            y = car_params[1]
            angle = car_params[2]
            color = car_params[3]
            car = PointCar(self, x, y, angle, canvas=self.get_canvas(), color=color)
            self.cars.append(car)

    # Render

    # TODO: putting cars on map, step, reset, render
    # TODO: in Robert's code, where it has `Canvas()`, just set that equal to the Map's canvas


# Loads a map from a JSON file, located at filepath 'filepath'
def load_map():
    prompt = 'Input the desired load location: (default: ../maps/test_map.json) Input: '
    input_str = ''
    try:
        if len(input_str) == 0:
            input_str = '../maps/test_map.json'
        map_dict = json.load(open(input_str, 'r'))
        return map_dict
        print "Loaded"
    except IOError as e:
        print e


if __name__ == "__main__":

    map_dict = load_map()


    h = ttk.Scrollbar(root, orient=HORIZONTAL)
    v = ttk.Scrollbar(root, orient=VERTICAL)
    canvas2 = Canvas(root, scrollregion=(0, 0, 1200, 1200), yscrollcommand=v.set, xscrollcommand=h.set)
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

    def run_manually(map):
        map.set_initial_state()
        pg.init()
        screen = pg.display.set_mode((512, 512))
        map.set_screen(screen)
        controller = Controller()
        clock = pg.time.Clock()
        counter = 1
        # Will run for 10 seconds
        done = False
        while not done and counter < 600:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    map.load_to_state(map.initial_state)
                    return
            action = controller.process_input(a)
            a.step(action)
            pg.display.update()
            clock.tick(30)
            print counter
            counter += 1
            if counter == 600:
                pg.quit()




    a = Map(is_tkrendered=True, canvas=canvas2, screen=None, map_dict=map_dict)


    frame = ttk.Frame(root)
    frame.grid(column=1, row=0, sticky=(N, S, E))
    editor_label = ttk.Label(frame, text="Editing Panel")
    editor_label.grid(column=0, row=1)
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

    runner_label = ttk.Label(frame, text="Run Options")
    runner_label.grid(column=0, row=11)
    save_button = ttk.Button(frame, text='Save', command = lambda: a.save('../maps/test_map.json'))
    save_button.grid(column=0, row=12)
    runner_button = ttk.Button(frame, text='Run Manually', command = lambda: run_manually(a))
    runner_button.grid(column=0, row=13)
    supervisor_button = ttk.Button(frame, text='Run Supervisor', command = lambda: run_supervisor(a))
    supervisor_button.grid(column=0, row=14)

    #### END MAKESHIFT SIDEPANEL

    canvas2.bind("<Enter>", lambda event: canvas2.focus_set())

    a.set_currently_editing('path')
    root.mainloop()
