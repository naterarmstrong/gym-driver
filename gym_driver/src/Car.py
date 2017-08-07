from read_config import read_config

from PIL import Image, ImageTk
import pygame as pg

configs = read_config()
#MAX_VEL = configs["MAX_VEL"]
#LEN_REAR = configs["LEN_REAR"]
#LEN_FRONT = configs["LEN_FRONT"]
#MASS = configs["MASS"]
#YAW_INTERTIA = configs["YAW_INTERTIA"]
MAX_VEL = 20
LEN_REAR = 25.0
LEN_FRONT = 25.0
MASS = 100.0
YAW_INTERTIA = 2510.15 * 25.0


COLORS = ['green', 'blue', 'grey', 'orange']
IMAGE_FORMATS = ['pg', 'tk']
ORIENTATIONS = [0, 90, 180, 270]
SCREEN_SIZE = 512
MAX_VEL = 20
USING_TK = True

def populate_car_images():
	car_images = {}
	for color in COLORS:
		car_images[color] = {}
		for orientation in ORIENTATIONS:
			car_images[color][orientation] = {}
			for image_format in IMAGE_FORMATS:
				car_images[color][orientation][image_format] = {}
				if image_format == 'pg':
					image = pg.image.load("../resources/{}_car.png".format(color))
					car_images[color][0][image_format] = image
				elif image_format == 'tk' and USING_TK:
					image = Image.open('../resources/{}_car.gif'.format(color)).rotate(orientation)
					car_images[color][orientation][image_format] = ImageTk.PhotoImage(image)
	return car_images


# Car class
class Car:

    car_images = populate_car_images()


    # Car constructor
    def __init__(self, map, x, y, angle, canvas=None, color='orange'):
        self.map = map
        self.x = x
        self.y = y
        self.angle = angle
        self.color = color
        self.vel = 0 # velocity
        self.acc = 0 # acceleration
        self.canvas = canvas

    
    # Renders the car to a pygame screen, if it's in an appropriate distance
    def save(self):
        x = self.x
        y = self.y
        angle = self.angle
        color = self.color
        return [x, y, angle, color]

    def render_to_pygame(self, screen, screen_coords):
        image = self.get_image('pg')
        coords = (self.x, self.y)
        if False:
        	pos = (256, 256)
        	screen.blit(image, pos)
        elif -(SCREEN_SIZE / 2) <= coords[0] - screen_coords[0]<= (SCREEN_SIZE / 2 + 50) and \
            -(SCREEN_SIZE / 2) <= coords[1] - screen_coords[1] <= (SCREEN_SIZE / 2 + 50):
            pos = (int(coords[0] - screen_coords[0]), int(coords[1] - screen_coords[1]))
            print pos
            #rotated_img = pg.transform.rotate(image, -self.get_angle())
            screen.blit(image, pos)
            pg.display.update()
        else:
            print "not rendered"
            pos = (int(coords[0] - screen_coords[0]), int(coords[1] - screen_coords[1]))
            print pos
            print '--------------------------'


    # Renders the car to a canvas
    def render_to_canvas(self):
    	# TODO:: FIX
    	image = self.get_image('tk')
    	id = self.canvas.create_image(self.x, self.y, image=image)
    	self.id = id
    	self._rendered = True


    # Updates the canvas render
    def update_canvas_render(self):
    	if not self._rendered:
    		return
    	image = self.get_image('tk')
    	self.canvas.itemconfigure(self.id, image=image)


    # Gets an image for use in either pygame or tk
    def get_image(self, image_type):
    	#TODO: Check that angles go in the right direction
    	angle = self.get_angle()
    	if angle % 90 == 0 and image_type == 'tk':
    		image = Car.car_images[self.color][angle][image_type]
    	else:
    		image=Car.car_images[self.color][0][image_type]


    	if image_type == 'pg':
    		image = pg.transform.rotate(image,-angle)
    	elif image_type == 'tk':
    		pass
    	else:
    		raise Exception("Unsupported Image Type: {}".format(image_type))
    	return image

    # Adds listeners
    def add_listeners(self):
    	self.canvas.tag_bind(self.id, "<Button-1>", self.on_leftclick)

    def on_leftclick(self):
    	currently_editing = self.map.get_currently_editing()
    	if currently_editing == 'cars':
    		self.delete_car()





    # Getter: Angle
    def get_angle(self):
    	return self.angle

    # Setter: Angle
    def set_angle(self, new_angle):
    	new_angle = new_angle % 360
    	self.angle = new_angle
