# fooling around with pygame --> draw/fill some rectangles
import pygame as pg
from tkinter import *
pg.init()
from Car import Car
# initiate pygame first
#create a 400x300 window
screen = pg.display.set_mode((400, 300))
# give it a title
pg.display.set_caption('FORDS Driving Simulator')
GRASS_GREEN = (25, 123, 48)
img = pg.image.load("../resources/quarter_turn_road_200.png")

#draw/fill a 77x33 rectangle in position x=250, y=50 (NW corner)
screen.fill(GRASS_GREEN)
screen.blit(img, (0, 0))
# hey, nothing gets displayed until one updates the screen
pg.display.update()
screen.blit(pg.transform.rotate(img, 90), (100, 100))
pg.display.update()
# create the event loop to get things going
# and specify an exit action (clicking on the window x)

car = Car(None, 50, 50, 0)
car.render_to_pygame(screen, (50, 50))


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            raise SystemExit
