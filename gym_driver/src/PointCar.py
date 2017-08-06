from numpy import sin, cos, deg2rad

from Car import Car, MAX_VEL

# PointCar class
class PointCar(Car):

    # Modify attributes to reflect one game step
    def step(self, action):
        if action is None:
            action_acc, action_angle = 0.0, 0.0
        action_acc, action_angle = action
        # Makes sure angle within (0, 360)
        self.angle = (self.angle + action_angle) % 360
        # Clamps acceleration
        self.acc = max(min(action_acc, MAX_VEL - self.vel), -self.vel)
        dist = self.vel + 0.5 * self.acc
        dx = dist * cos(deg2rad(self.angle))
        dy = dist * sin(deg2rad(self.angle))
        self.x += dx
        self.y += dy
        self.vel = max(min(self.vel + self.acc, MAX_VEL), 0)
