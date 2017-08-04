from numpy import arange, sqrt, sin, cos, tan, arctan, deg2rad, rad2deg
from scipy.integrate import odeint

from Car import Car, MAX_VEL, LEN_REAR, LEN_FRONT, MASS, YAW_INTERTIA

# DynamicCar class
class DynamicCar(Car):

    # DynamicCar constructor
    def __init__(self, map, x, y, angle):
        Car.__init__(map, x, y, angle)
        self.d_angle = 0
        self.d_x = 0
        self.d_y = 0

    # Modify attributes to reflect one game step
    def step(self, action_acc, action_angle):
        # Pre-process actions
        action_angle = deg2rad(action_angle)
        angle = deg2rad(self.angle)
        d_angle = deg2rad(self.d_angle)
        friction = self.map.get_point_friction(self.x, self.y)
        # Solve differential equations
        t = arange(0.0, 1.0, 0.1)
        ode_state = (self.x, self.y, self.d_x, self.d_y, angle, d_angle)
        aux_state = (friction, action_acc, action_angle)
        deltas = odeint(self.integrate, ode_state, t, args=aux_state)
        x, y, d_x, d_y, angle, d_angle = deltas[-1]
        self.x, self.y, self.d_x, self.d_y = x, y, d_x, d_y
        self.vel = sqrt(self.d_x ** 2 + self.d_y ** 2)
        self.angle = rad2deg(angle) % 360
        self.d_angle = (d_angle) % 360

    # Calculate numerical values for variables in the differential equation
    @staticmethod
    def integrate(state, t, friction, action_acc, action_angle):
        # Extract the state
        x, y, d_x, d_y, angle, d_angle = state
        vel = sqrt(d_x ** 2 + d_y ** 2)
        # Calculate slip angle
        beta = arctan((LEN_REAR / (LEN_REAR + LEN_FRONT)) * tan(action_angle))
        slip_angle = (vel / LEN_REAR) * sin(beta)
        slip_front = -slip_angle
        slip_rear = 0
        # Calculate tire cornering stiffness
        cornering_force = MASS * (LEN_REAR / (LEN_REAR + LEN_FRONT))
        cr_f = -friction * cornering_force * slip_front
        cr_r = -friction * cornering_force * slip_rear
        # Calculate deltas
        d_x = d_x * cos(angle) - d_y * sin(angle)
        d_y = d_x * sin(angle) + d_y * sin(angle)
        dd_x = d_angle * d_y + action_acc
        dd_y = -d_angle * d_x + (2 / MASS) * (cr_f * cos(action_angle) + cr_r)
        dd_angle = (2 / YAW_INTERTIA) * (LEN_FRONT * cr_f - LEN_REAR * cr_r)
        # Clamp acceleration
        acc = sqrt((dd_x + d_x) ** 2 + (dd_y + d_y) ** 2)
        if acc > MAX_VEL:
            a = dd_x ** 2 + dd_y ** 2
            b = 2 * (dd_x * d_x + dd_y + d_y)
            c = d_x ** 2 + d_y ** 2 - MAX_VEL ** 2
            max_fraction = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
            dd_x *= max_fraction
            dd_y *= max_fraction
        # Clamp velocity
        if vel > MAX_VEL:
            max_fraction = MAX_VEL / vel
            d_x *= max_fraction
            d_y *= max_fraction
        return d_x, d_y, dd_x, dd_y, d_angle, dd_angle
