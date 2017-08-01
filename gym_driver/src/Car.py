# Car class
class Car:

    # Car constructor
    def __init__(self, map, x, y, angle, mass):
        self.map = map
        self.x = x
        self.y = y
        self.angle = angle
        self.vel = 0 # velocity
        self.acc = 0 # acceleration
        self.mass = mass
