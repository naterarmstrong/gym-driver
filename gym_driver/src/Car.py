from read_config import read_config

configs = read_config()
MAX_VEL = configs["MAX_VEL"]
LEN_REAR = configs["LEN_REAR"]
LEN_FRONT = configs["LEN_FRONT"]
MASS = configs["MASS"]
YAW_INTERTIA = configs["YAW_INTERTIA"]

# Car class
class Car:

    # Car constructor
    def __init__(self, map, x, y, angle):
        self.map = map
        self.x = x
        self.y = y
        self.angle = angle
        self.vel = 0 # velocity
        self.acc = 0 # acceleration
