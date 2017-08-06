from numpy import arange, sin, cos, tan, arctan, deg2rad, rad2deg
from scipy.integrate import odeint

from Car import Car, MAX_VEL, LEN_REAR, LEN_FRONT

# KinematicCar class
class KinematicCar(Car):

    # Modify attributes to reflect one game step
    def step(self, action):
        action_acc, action_angle = action
        # Pre-process actions
        action_angle = deg2rad(action_angle)
        angle = deg2rad(self.angle)
        action_acc = max(min(action_acc, MAX_VEL - self.vel), -self.vel)
        # Solve differential equations
        t = arange(0.0, 1.0, 0.1)
        ode_state = (self.x, self.y, self.vel, angle)
        aux_state = (action_acc, action_angle)
        deltas = odeint(self.integrate, ode_state, t, args=aux_state)
        x, y, vel, angle = deltas[-1]
        self.x, self.y, self.vel, self.angle = x, y, vel, rad2deg(angle) % 360

    # Calculate numerical values for variables in the differential equation
    @staticmethod
    def integrate(state, t, action_acc, action_angle):
        # Extract the state
        x, y, vel, angle = state
        # Calculate deltas
        beta = arctan((LEN_REAR / (LEN_REAR + LEN_FRONT)) * tan(action_angle))
        d_x = vel * cos(angle + beta)
        d_y = vel * sin(angle + beta)
        delta_vel = action_acc
        d_angle = (vel / LEN_REAR) * sin(beta)
        return d_x, d_y, delta_vel, d_angle
